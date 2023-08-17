# Importar las clases
from Cliente import *
from Persona import *
from Producto import *

# Lista para almacenar los clientes
clientes = []

# Lista para almacenar las personas
personas = []
personas.append(Persona("12345678", "Alexander", "Guevara"))
personas.append(Persona("98765432", "Josue", "Campos"))

# Función para imprimir el menú
def imprimir_menu():
    print("***** MENÚ *****")
    print("1. LISTAR PRODUCTOS")
    print("2. AGREGAR PRODUCTOS")
    print("3. HACER UNA VENTA")
    print("4. AGREGAR CLIENTE")
    print("5. SALIR")


# Función para el inicio de sesión
def inicio_sesion():
    dni_ingresado = input("Ingresa tu DNI: ")
    for persona in personas:
        if persona.dni == dni_ingresado:
            print(f"Bienvenido {persona.nombre} {persona.apellidos}")
            return True
    print("DNI no encontrado.")
    return False

# Crear listas vacías para los productos
productos_desayuno = []
productos_almuerzo = []
productos_cena = []

# Agregar productos de desayuno usando append
productos_desayuno.append(Desayuno("Croissant", 2.50, "Continental", 10))
productos_desayuno.append(Desayuno("Huevos Revueltos", 3.75, "Americano", 8))
productos_desayuno.append(Desayuno("Tostadas con Aguacate", 4.50, "Saludable", 15))
productos_desayuno.append(Desayuno("Panqueques", 3.25, "Clásico", 12))
productos_desayuno.append(Desayuno("Omelette", 4.00, "Variado", 10))

# Agregar productos de almuerzo usando append
productos_almuerzo.append(Almuerzo("Pollo a la Parrilla", 8.50, "Especialidad", 20))
productos_almuerzo.append(Almuerzo("Pasta Carbonara", 7.25, "Italiano", 18))
productos_almuerzo.append(Almuerzo("Ensalada César", 6.75, "Light", 25))
productos_almuerzo.append(Almuerzo("Burger con Papas Fritas", 7.00, "Americano", 22))
productos_almuerzo.append(Almuerzo("Sushi Variado", 9.00, "Japonés", 16))

# Agregar productos de cena usando append
productos_cena.append(Cena("Salmón a la Plancha", 10.50, "Saludable", 15))
productos_cena.append(Cena("Filete Mignon", 12.75, "Gourmet", 10))
productos_cena.append(Cena("Pizza Margherita", 8.25, "Italiano", 18))
productos_cena.append(Cena("Tacos de Pescado", 9.00, "Mexicano", 20))
productos_cena.append(Cena("Sopa de Tomate", 6.50, "Clásico", 15))


# Función para listar los productos
def listar_productos():
    print("***** LISTA DE PRODUCTOS *****")
    print("\n{:<40} | {:<15} | {:<10}".format("Nombre", "Precio", "Cantidad"))
    print("=" * 75)
    
    # Lista de productos de desayuno
    print("\nDesayuno:")
    for producto in productos_desayuno:
        print("{:<40} | ${:<15.2f} | {:<10}".format(producto.nombre, producto.precio, producto.cantidad))
    
    # Lista de productos de almuerzo
    print("\nAlmuerzo:")
    for producto in productos_almuerzo:
        print("{:<40} | ${:<15.2f} | {:<10}".format(producto.nombre, producto.precio, producto.cantidad))
    
    # Lista de productos de cena
    print("\nCena:")
    for producto in productos_cena:
        print("{:<40} | ${:<15.2f} | {:<10}".format(producto.nombre, producto.precio, producto.cantidad))

# Función para agregar productos
def agregar_productos():
    # Pedir al usuario que ingrese los detalles del nuevo producto
    nombre_producto = input("Ingresa el nombre del producto: ")
    
    # Buscar si el producto ya existe en la lista de productos
    producto_existente = None
    for producto in productos_desayuno + productos_almuerzo + productos_cena:
        if producto.nombre == nombre_producto:
            producto_existente = producto
            break
    
    if producto_existente:
        # Si el producto ya existe, preguntar si se desea agregar más cantidad
        respuesta = input(f"El producto '{nombre_producto}' ya existe. ¿Desea agregar más cantidad? (S/N): ")
        if respuesta.lower() == "s":
            cantidad_adicional = int(input(f"Ingresa la cantidad adicional del producto '{nombre_producto}': "))
            producto_existente.agregar_cantidad(cantidad_adicional)  # Agregar la cantidad adicional al producto existente
            print(f"Se agregó {cantidad_adicional} unidades más a '{nombre_producto}'.")
        else:
            print(f"El producto '{nombre_producto}' ya existe.")
    else:
        # Si el producto no existe, solicitar información adicional y crear un nuevo producto
        precio_producto = float(input("Ingresa el precio del producto: "))
        cantidad_producto = int(input("Ingresa la cantidad del producto: "))
        
        tipo_producto = input("Ingresa el tipo de producto (Desayuno/Almuerzo/Cena): ")
        nuevo_producto = Producto(nombre_producto, precio_producto, cantidad_producto)
        
        # Agregar el nuevo producto a la lista correspondiente según el tipo
        if tipo_producto.lower() == "desayuno":
            productos_desayuno.append(nuevo_producto)
        elif tipo_producto.lower() == "almuerzo":
            productos_almuerzo.append(nuevo_producto)   
        elif tipo_producto.lower() == "cena":
            productos_cena.append(nuevo_producto)
        else:
            print("Tipo de producto no válido.")


# Función para formatear los datos de la venta
def datos_venta(nombre_producto, cantidad, nombre_cliente, apellidos_cliente, dni_cliente):
    return f"**********************************\n" \
           f"        TICKET DE VENTA\n" \
           f"**********************************\n" \
           f"Producto: {nombre_producto}\n" \
           f"Cantidad: {cantidad}\n" \
           f"Cliente: {nombre_cliente} {apellidos_cliente}\n" \
           f"DNI: {dni_cliente}\n" \
           f"**********************************" 
# Función para hacer una venta
def hacer_venta():
    # Solicitar al usuario el DNI del cliente
    dni_cliente = input("Ingresa el DNI del cliente: ")
    
    # Buscar si el cliente existe en la lista de clientes
    cliente_existente = None
    for cliente in clientes:
        if cliente.get_dni() == dni_cliente:
            cliente_existente = cliente
            break
    
    if cliente_existente:
        productos_venta = []  # Lista para almacenar los productos vendidos
        subtotal = 0
        
        # Ciclo para agregar productos a la venta
        while True:
            nombre_producto = input("Ingresa el nombre del producto que deseas vender (o 'no' para finalizar): ")
            if nombre_producto.lower() == "no":
                break
            
            # Buscar si el producto existe en la lista de productos
            producto_existente = None
            # Iterar sobre la lista de productos (desayuno, almuerzo, cena)
            for producto in productos_desayuno + productos_almuerzo + productos_cena:
                # Comprobar si el nombre del producto coincide con el nombre ingresado
                if producto.nombre == nombre_producto:
                    # Si se encuentra un producto con el mismo nombre, se guarda en producto_existente
                    producto_existente = producto
                    break  # Se interrumpe el bucle ya que se encontró el producto

            
            # Verificar si el producto existe en la lista de productos
            if producto_existente:
                # Solicitar al usuario la cantidad de producto deseada
                cantidad_deseada = int(input(f"Ingrese la cantidad de '{nombre_producto}' que deseas vender: "))
                
                # Verificar si la cantidad deseada está disponible en el inventario
                if cantidad_deseada <= producto_existente.cantidad:
                    # Actualizar la cantidad del producto en el inventario
                    producto_existente.cantidad -= cantidad_deseada
                    # Agregar el producto vendido a la lista de productos de la venta
                    productos_venta.append((nombre_producto, cantidad_deseada, producto_existente.get_precio()))
                    # Calcular el subtotal sumando el precio del producto vendido
                    subtotal += cantidad_deseada * producto_existente.get_precio()
                else:
                    print("No hay suficiente cantidad disponible para la venta.")
            else:
                print(f"El producto '{nombre_producto}' no existe en el inventario.")


        
        # Imprimir el ticket de venta
        print("\nTICKET DE VENTA")
        print("***********************")
        for producto, cantidad, precio_unitario in productos_venta:
            print(f"Producto: {producto}")
            print(f"Cantidad: {cantidad}")
            print(f"Precio unitario: ${precio_unitario:.2f}")
            print("***********************")
        
        total = subtotal
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Total: ${total:.2f}")
    else:
        print("El DNI del cliente no se encuentra registrado.")

# Inicio de sesión
while not inicio_sesion():
    pass  # Repetir hasta que el inicio de sesión sea exitoso

# Función para agregar un cliente
def agregar_cliente():
    # Solicitar al usuario los datos del cliente
    nombre = input("Ingresa el nombre del cliente: ")
    apellidos = input("Ingresa los apellidos del cliente: ")
    dni = input("Ingresa el DNI del cliente: ")
    
    # Crear una instancia de la clase Cliente con los datos proporcionados por el usuario
    nuevo_cliente = Cliente(nombre, apellidos, dni)
    
    # Agregar el nuevo cliente a la lista de clientes
    clientes.append(nuevo_cliente)
    
    # Imprimir un mensaje confirmando la adición del cliente
    print(f"Se ha agregado al cliente: {nuevo_cliente.get_nombre()} {nuevo_cliente.get_apellidos()} (DNI: {nuevo_cliente.get_dni()})")


# Menú principal
while True:
    # Imprimir el menú para que el usuario pueda ver las opciones
    imprimir_menu()

    # Pedir al usuario que seleccione una opción
    opcion = input("Selecciona una opción: ")

    # Evaluar la opción seleccionada por el usuario
    if opcion == "1":
        listar_productos()  # Llamar a la función para listar productos
    elif opcion == "2":
        agregar_productos()  # Llamar a la función para agregar productos
    elif opcion == "3":
        hacer_venta()  # Llamar a la función para hacer una venta
    elif opcion == "4":
        agregar_cliente()  # Llamar a la función para agregar un cliente
    elif opcion == "5":
        print("Saliendo del programa...")  # Salir del programa
        break  # Romper el ciclo while y finalizar el programa
    else:
        print("Opción no válida. Inténtalo de nuevo.")  # Mensaje en caso de opción inválida

