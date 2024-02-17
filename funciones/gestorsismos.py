import ui.titles as t
import ui.menus as m
import os
from tabulate import tabulate

def regCiudad(sismos: list):
    while len(sismos) < 5:
        t.headerRegciudad()
        print('Ciudades registradas:\n')
        for idx, item in enumerate(sismos):
            print(f'{idx+1}. {item[0]}')
        ciudad = input('\nIngrese el Nombre de la Ciudad: ').capitalize()
        isCiudad = False
        for item in sismos:
            if ciudad == item[0]:
                isCiudad = True
                break
        if isCiudad:
            print('Esta ciudad ya se encuentra registrada')
            os.system('pause')
            os.system('cls')
        else:
            sismos.append([ciudad, []])
            os.system('cls')
    os.system('pause')


def regSismo(sismos : list, contSis : int):
    m.menuRegSis(sismos)
    for idx, item in enumerate(sismos): 
        isSismo = True
        isMensaje = False
        while isSismo:
            if idx > 0 and not isMensaje:
                    os.system('cls')
                    print(f'Debe ingresar {contSis} sismos en las siguientes ciudades')
                    isMensaje = True
            try:
                sismo = float(input(f'Ingrese el sismo de la ciudad {item[0]}: '))
            except ValueError:
                print('Dato invalido')
            else:
                if sismo <= 0:
                    print('El sismo no puede tener rangos negativos o iguales a 0')
                else:
                    if idx > 0:
                        item[1].append(sismo)
                        n-=1
                        if n == 0:
                            n = contSis
                            os.system('cls')
                            isSismo = False
                    else:
                        contSis+= 1
                        n = contSis
                        item[1].append(sismo)
                        isSismo = bool(input('¿Desea ingresar otro sismo a la ciudad actual? (S(si)/Enter(No)) '))

def buscarSismos(sismos: list):
    t.headerInforme()
    ciudad = input('Ingrese el nombre de la ciudad a buscar: ').capitalize()
    isSearch = False
    for idx, item in enumerate(sismos):
        if ciudad == item[0]:
            isSearch = True
            print(tabulate([item], headers=['Ciudad', 'Sismos'], tablefmt='grid'))
            break
    if not isSearch:
        print('La ciudad ingresada no se encuentra en la lista de sismos.')
    os.system('pause')


from tabulate import tabulate

def informeRiesgo(sismos: list):
    t.headerInforme() 
    riesgo = []
    for ciudad, sismos in sismos:
        promedio = sum(sismos) / len(sismos)
        nivelRiesgo = ''
        if promedio < 2.5:
            nivelRiesgo = 'Amarillo (Sin riesgo)'
        elif 2.5 <= promedio <= 4.5:
            nivelRiesgo = 'Naranja (Riesgo Medio)'
        else:
            nivelRiesgo = 'Rojo (Riesgo)'
        riesgo.append([ciudad, promedio, nivelRiesgo])

    print(tabulate(riesgo, headers=['Ciudad', 'Promedio de Sismos', 'Nivel de Riesgo'], tablefmt='grid'))
    os.system('pause')


