# # Crear un diccionario para almacenar las listas
# diccionario_listas = {}

# while True:
#     nombre_lista = input("Por favor, ingresa un nombre para la nueva lista (o 'salir' para terminar): ")
    
#     # Verificar si se desea salir del programa
#     if nombre_lista.lower() == "salir":
#         break
    
#     # Crear una lista vacía
#     nueva_lista = []
    
#     # Agregar elementos a la lista
#     while True:
#         elemento = input("Ingresa un elemento para la lista (o 'fin' para terminar): ")
#         if elemento.lower() == "fin":
#             break
#         nueva_lista.append(elemento)
    
#     # Almacenar la lista en el diccionario
#     diccionario_listas[nombre_lista] = nueva_lista

# # Imprimir el contenido de todas las listas almacenadas
# for nombre, lista in diccionario_listas.items():
#     print(f"La lista {nombre} contiene: {lista}")
# print(diccionario_listas)
