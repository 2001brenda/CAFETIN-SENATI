from producto import Producto 
from utilitarios import input_int

menu = """
CAFETIN SENATI
________________
OPCIONES:

1. Desayuno
2. Almuerzo
3. Cena
4, Salir
"""

lista_desayunos = []
lista_almuerzos = []
lista_cenas = []

def crear_producto(list_product):
    nombre_p = input("Nombre del producto: ")
    precio_p = input_int("Precio del producto: ", "No ingresaste bien el precio")
    stock_p = input_int("Stock del producto: ", "No ingresaste bien el stock")
    item_p = Producto(nombre_p, precio_p, stock_p)
    list_product.append(item_p)
    
p = Producto("Jugo de Quinua", 2, 50 )
c = Producto("Pan con palta", 2, 50)
lista_desayunos.append(p)
lista_desayunos.append(c)
 

s = Producto("Seco de pollo", 7, 50 )
b = Producto("Chifa", 10, 50)
lista_almuerzos.append(s)
lista_almuerzos.append(b) 

  
t = Producto("Lomo saltado", 8, 50 )
u = Producto("Pollo broaster", 15, 50)
lista_cenas.append(t)
lista_cenas.append(u)


def listar_productos(list_product):
    contador = 0
    for item in list_product:
        contador += 1
        print(f"{contador}. {item.get_info_completa()}")
    
def vender_producto(product_selected, cantidad):
    product_selected.actualizar_stock(cantidad)
    
def ticket_venta(nombre_p, cantidad_p, sub_total):
    t = f"""
    CAFETIN SENATI
    TICKET DE VENTA
    PRODUCTO           CANTIDAD        SUB, TOTAL
    
    1. { nombre_p }      {cantidad_p}     {sub_total}
    """
    
    return
        
print(menu)
        
opcion = input_int("Elija una opcion: ", "No existe esta opcion")
if opcion == 1:
    listar_productos(lista_desayunos)
    opcion_desayuno = input_int("Elija un opcion: ", "No existe esta opcion")
    producto_seleccionado = lista_desayunos[opcion_desayuno - 1]
    pregunta = input_int("Cual es la cantidad que desea: ", "No existe esta opcion")
    vender_producto(producto_seleccionado, pregunta)
    subtotal = producto_seleccionado.get_precio() * pregunta 
    print(ticket_venta(producto_seleccionado.get_nombre(), pregunta, subtotal))
    
elif opcion == 2:
    listar_productos(lista_almuerzos)
elif opcion == 3:
    listar_productos(lista_cenas)
