from producto import listarproductos

def menu():
    lista_de_productos = [{'nombre': 'Cafe', 'costo': "S/.5"},
        {'nombre': 'Empanada de queso', 'costo': "S/.3"}
    ]

omenu = """
CAFETIN SENATI
________________
OPCIONES:
1. Desayuno
2. Almuerzo
3. Cena
4, Salir
"""
flag  = True
while flag:
    try:
        print(omenu)
        opcion = int(input("Elige una opcion: "))
    except ValueError:
        print("Has elegido una opcion que no esta en el menu")
    else:
        if opcion == 1:
            print("Categoria Desayuno")
            print(Producto.info)
        elif opcion == 2:
            print("Categoria Alumerzo")
        elif opcion == 3:
            print("Categoria Cena")
        elif opcion == 4:
            print("Saliendo")
            flag = False
