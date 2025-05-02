class Empleado:
    """Clase que representa a un empleado con nombre e identificación."""
    
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
    
    def __str__(self):
        return f"{self.identificacion},{self.nombre}"
    
    @staticmethod
    def from_string(line):
        """Crea un objeto Empleado a partir de una línea de texto."""
        parts = line.strip().split(',')
        if len(parts) == 2:
            return Empleado(parts[1], parts[0])
        return None