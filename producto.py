class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def info(self):
        return f"{self.nombre} {self.stock}"
    
    def actualizar_stock(self, stock_vendida):
        self.stock = self.stock - stock_vendida
    
    def get_nombre(self):
        return self.nombre
    
    def get_info_completa(self):
        return f"{ self.nombre } { self.precio } { self.stock }"
