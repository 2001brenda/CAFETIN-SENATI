class Cliente:
    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_apellidos(self):
        return self.apellidos
    
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        self.dni = dni
