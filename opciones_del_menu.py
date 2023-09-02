import os
import datetime
import time
from rich import print
from rich.table import Table

def comprobar_precio(servicio):
    while True:
        try:
            while True:
                precio_del_servicio = float(input(f'Precio del servicio {servicio}: '))
                if precio_del_servicio > 0:
                    break
                else:
                    print('El precio tiene que ser mayor a 0\n')
        except ValueError:
            print('Ese no es un número válido. Intenta de nuevo\n')
        except Exception as ex:
            print(f'Ocurrió el error: {ex}. Intente de nuevo\n')
        else:
            break
    
    return precio_del_servicio


class RegistrarNota:
    def __init__(self, folio):

        self.detalles_de_nota()
        self.detalles_de_nota_a_str()
        self.retornar_datos()
        self.mostrar_nota(folio)
                

    def detalles_de_nota(self):
        os.system('cls')
        print('[#7AFFFF]--Registro de la Nota--[#/7AFFFF]\n')
        print('[#9999FF](Separados por comas)[#/9999FF]')
        self.servicios = input('Servicios a realizar: ')

        self.monto_total = 0
        self.servicios_y_precio = {}

        print('\n([#9999FF]En número entero o con decimales, mayor a cero)[#/9999FF]')

        for servicio in self.servicios.split(','):
            servicio = servicio.strip()

            precio_del_servicio = comprobar_precio(servicio)

            self.servicios_y_precio[servicio] = precio_del_servicio
            self.monto_total += precio_del_servicio

        self.nombre_del_cliente = input('\nNombre del cliente: ')

    def detalles_de_nota_a_str(self):
        self.detallesNota = '[#9999FF]|[/#9999FF] '
        for k,v in self.servicios_y_precio.items():
            self.detallesNota += f'{k}: {v} [#9999FF]|[/#9999FF] '
        

    def retornar_datos(self):

        self.fecha_actual = str (datetime.date.today())

        datos_recolectados = (self.fecha_actual, self.nombre_del_cliente, self.detallesNota)

        return datos_recolectados


    def mostrar_nota(self, folio):
        os.system('cls')

        nota = Table(title='[#7AFFFF]--Nueva nota registrada--[/#7AFFFF]', )
    
        nota.add_column("Detalles", justify="left", style="#9999FF")
        nota.add_column("Datos", justify="left", style="white")

        nota.add_row('Folio', f'{folio}')
        nota.add_row('Fecha', f'{self.fecha_actual}')
        nota.add_row('Nombre del cliente', f'{self.nombre_del_cliente}')
        nota.add_row('Monto a pagar', f'{self.monto_total}')
        nota.add_row('Detalle de nota', f'{self.detallesNota}')

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