from producto import Producto 
from cliente import Cliente
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

jq = Producto("Jugo de Quinua", 2, 50)

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
    
def ticket_venta(nombre_p, cantidad_p, sub_total, client):
    t = f"""
                        CAFETIN SENATI
                        - - - - - - - - 
                        TICKET DE VENTA
                        ________________
                        
    cliente: { client }
    
    PRODUCTO             CANTIDAD        SUB TOTAL
    
1. { nombre_p }           {cantidad_p}             {sub_total}
    """
    
    return t

def crear_cliente(list_client):
    nombre_c = input("Nombre del cliente: ")
    dni_c = input(" DNI del cliente: ")
    cliente_c = Cliente (nombre_c, dni_c)
    list_client.append(cliente_c)
    
lista_clientes = []
        
print(menu)
        
opcion = input_int("Elija una opcion: ", "No existe esta opcion")
if opcion == 1:
    listar_productos(lista_desayunos)
    opcion_desayuno = input_int("Elija un opcion: ", "No existe esta opcion")
    producto_seleccionado = lista_desayunos[opcion_desayuno - 1]
    pregunta = input_int("Cual es la cantidad que desea: ", "No existe esta opcion")
    vender_producto(producto_seleccionado, pregunta)
    subtotal = producto_seleccionado.get_precio() * pregunta 
    cliente = input("digite el nombre del cliente")
    #exist_client= input ("el cliente existe si/no: ")
    #if exist_client == "si":
        
    print(ticket_venta(producto_seleccionado.get_nombre(), pregunta, subtotal, cliente ))
    
elif opcion == 2:
    listar_productos(lista_almuerzos)
elif opcion == 3:
    listar_productos(lista_cenas)
