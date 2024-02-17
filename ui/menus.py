import os
import ui.titles as t

def menuMain():
    opciones = ['Registrar Ciudad','Registrar Sismo','Buscar sismos por ciudad','Informe de riesgo','Salir']
    t.headerMain()
    for i, item in enumerate(opciones):
                print(f'{i+1}. {item}')

def menuRegSis(sismos : list):
    t.headerRegsismo()   
    print('Ciudades registradas: \n')
    for idx, item in enumerate(sismos):
        print(f'{idx+1}. {item[0]}')    