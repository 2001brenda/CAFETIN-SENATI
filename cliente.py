class Cliente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        
    def get_dni (self):
        return f" {self.dni}"
