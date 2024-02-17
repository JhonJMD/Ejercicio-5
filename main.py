import os
import ui.menus as m
import funciones.gestorsismos as fun
import funciones.borrarPantalla as osl

if __name__ == '__main__':
    sismos = []
    contSis = 0
    isActive = True
    while isActive:
            os.system('cls')
            try:
                m.menuMain()
                op = int(input(': '))
            except ValueError:
                print('Dato no valido')
                os.system('pause')
                os.system('cls')
            else:
                if op == 1:
                    os.system('cls')
                    fun.regCiudad(sismos)
                elif op == 2:
                    os.system('cls')
                    fun.regSismo(sismos, contSis)
                elif op == 3:
                    os.system('cls')
                    fun.buscarSismos(sismos)
                elif op == 4:
                    os.system('cls')
                    fun.informeRiesgo(sismos)
                elif op == 5:
                    os.system('cls')
                    print('Gracias por utilizar nuestro sistema, Vuelve pronto.....')
                    isActive = False
                else:
                    print('Opción incorrecta')
                    os.system('pause')
                    os.system('cls')