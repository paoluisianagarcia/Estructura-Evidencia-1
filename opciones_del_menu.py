import os
import datetime
import time
from rich import print
from rich.table import Table

class RegistrarNota:
    def __init__(self, folio):

        self.detalles_de_nota()
        self.retornar_datos()
        self.mostrar_nota(folio)
                

    def detalles_de_nota(self):
        os.system('cls')
        print('[#7AFFFF]--Registro de la Nota--[#/7AFFFF]\n')
        print('[#9999FF](Separados por comas)[#/9999FF]')
        self.servicios = input('Servicios a realizar: ')

        while True:
            try:
                self.monto = 0
                print('\n([#9999FF]En número entero o con decimales)[#/9999FF]')
                for servicio in self.servicios.split(','):
                    servicio = servicio.strip()
                    self.monto += float(input(f'Precio del servicio {servicio}: '))
            except ValueError:
                print('Ese no es un número válido. Intenta de nuevo')
            except Exception as ex:
                print(f'Ocurrió el error: {ex}. Intente de nuevo') 
            else:
                if self.monto > 0:
                    break
                else:
                    print('El precio tiene que ser mayor a 0')

        self.nombre_del_cliente = input('\nNombre del cliente: ')

    def retornar_datos(self):

        self.fecha_actual = str (datetime.date.today())

        datos_recolectados = (self.fecha_actual, self.nombre_del_cliente, self.servicios, self.monto)

        return datos_recolectados

    def mostrar_nota(self, folio):
        os.system('cls')

        nota = Table(title='[#7AFFFF]--Nueva nota registrada--[/#7AFFFF]', )
    
        nota.add_column("Detalles", justify="left", style="#9999FF")
        nota.add_column("Datos", justify="left", style="white")

        nota.add_row('Folio', f'{folio}')
        nota.add_row('Fecha', f'{self.fecha_actual}')
        nota.add_row('Nombre del cliente', f'{self.nombre_del_cliente}')
        nota.add_row('Servicio a realizar', f'{self.servicios}')
        nota.add_row('Monto a pagar', f'{self.monto}')

        print(nota, '\n')
    
    def aceptacion_de_nota(self):
        while True:
            aceptar = input('| a - Aceptar | c - Cancelar |\n\n')
            print()
            if aceptar.upper() in ('A', 'ACEPTAR'):
                for i in range(3):
                    time.sleep(.3)
                    print('[green].[/green]', end='  ')

                print('[green]Nota aceptada[/green]')
                time.sleep(.8)

                return True
            
            elif aceptar.upper() in ('C', 'CANCELAR'):
                for i in range(3):
                    time.sleep(.3)
                    print('[red].[/red]', end='  ')

                print('[red]Nota cancelada[/red]')
                time.sleep(.8)

                return False
            else:
                print('Opción no válida. Intente de nuevo')