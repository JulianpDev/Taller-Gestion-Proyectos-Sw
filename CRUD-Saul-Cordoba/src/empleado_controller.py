from empleado import Empleado
from empleado_repository import EmpleadoRepository

class EmpleadoController:
    """Controlador para manejar las operaciones de empleados."""
    
    def __init__(self):
        self.repository = EmpleadoRepository()
    
    def crear_empleado(self, nombre, identificacion):
        """Crea un nuevo empleado."""
        empleado = Empleado(nombre, identificacion)
        return self.repository.crear_empleado(empleado)
    
    def listar_empleados(self):
        """Lista todos los empleados."""
        return self.repository.listar_empleados()
    
    def editar_nombre_empleado(self, identificacion, nuevo_nombre):
        """Edita solo el nombre de un empleado."""
        return self.repository.editar_nombre_empleado(identificacion, nuevo_nombre)
    
    def eliminar_empleado(self, identificacion):
        """Elimina un empleado por su identificación."""
        return self.repository.eliminar_empleado(identificacion)