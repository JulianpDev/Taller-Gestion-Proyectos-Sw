import os
from empleado import Empleado

class EmpleadoRepository:
    """Clase que maneja el almacenamiento de empleados en un archivo de texto."""
    
    def __init__(self):
        # Obtener la ruta del directorio del script actual
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Crear la ruta del archivo en el mismo directorio
        self.ARCHIVO = os.path.join(script_dir, "empleados.txt")
    
    def crear_empleado(self, empleado):
        """Crea un nuevo empleado y lo guarda en el archivo."""
        empleados = self.listar_empleados()
        
        # Verificar si ya existe un empleado con esa identificación
        for emp in empleados:
            if emp.identificacion == empleado.identificacion:
                return False  # Ya existe un empleado con esa identificación
        
        # Agregar el nuevo empleado al archivo
        try:
            with open(self.ARCHIVO, 'a') as file:
                file.write(str(empleado) + '\n')
            return True
        except Exception as e:
            print(f"Error al crear empleado: {e}")
            return False
    
    def listar_empleados(self):
        """Lista todos los empleados almacenados en el archivo."""
        empleados = []
        
        # Crear el archivo si no existe
        if not os.path.exists(self.ARCHIVO):
            try:
                open(self.ARCHIVO, 'w').close()
            except Exception as e:
                print(f"Error al crear archivo: {e}")
                return empleados
        
        # Leer todos los empleados del archivo
        try:
            with open(self.ARCHIVO, 'r') as file:
                for line in file:
                    if line.strip():  # Ignorar líneas vacías
                        empleado = Empleado.from_string(line)
                        if empleado:
                            empleados.append(empleado)
        except Exception as e:
            print(f"Error al leer empleados: {e}")
        
        return empleados
    
    def editar_nombre_empleado(self, identificacion, nuevo_nombre):
        """Edita solo el nombre de un empleado existente."""
        empleados = self.listar_empleados()
        encontrado = False
        
        # Buscar y actualizar el empleado
        for emp in empleados:
            if emp.identificacion == identificacion:
                emp.nombre = nuevo_nombre
                encontrado = True
                break
        
        if not encontrado:
            return False
        
        # Reescribir todo el archivo con la información actualizada
        try:
            with open(self.ARCHIVO, 'w') as file:
                for emp in empleados:
                    file.write(str(emp) + '\n')
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False
    
    def eliminar_empleado(self, identificacion):
        """Elimina un empleado por su identificación."""
        empleados = self.listar_empleados()
        encontrado = False
        
        # Filtrar los empleados, excluyendo el que se va a eliminar
        empleados_filtrados = []
        for emp in empleados:
            if emp.identificacion == identificacion:
                encontrado = True
            else:
                empleados_filtrados.append(emp)
        
        if not encontrado:
            return False
        
        # Reescribir todo el archivo sin el empleado eliminado
        try:
            with open(self.ARCHIVO, 'w') as file:
                for emp in empleados_filtrados:
                    file.write(str(emp) + '\n')
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False