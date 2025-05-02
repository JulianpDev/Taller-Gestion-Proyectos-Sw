import os
import time
from empleado_controller import EmpleadoController

# Clase para añadir colores en la terminal
class Colores:
    RESET = '\033[0m'
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'
    
    NEGRO = '\033[30m'
    ROJO = '\033[31m'
    VERDE = '\033[32m'
    AMARILLO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIAN = '\033[36m'
    BLANCO = '\033[37m'
    
    FONDO_NEGRO = '\033[40m'
    FONDO_ROJO = '\033[41m'
    FONDO_VERDE = '\033[42m'
    FONDO_AMARILLO = '\033[43m'
    FONDO_AZUL = '\033[44m'
    FONDO_MAGENTA = '\033[45m'
    FONDO_CIAN = '\033[46m'
    FONDO_BLANCO = '\033[47m'

def limpiar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo(texto):
    """Muestra un título formateado."""
    ancho = 50
    print(Colores.FONDO_AZUL + Colores.BLANCO + Colores.NEGRITA)
    print(texto.center(ancho))
    print(Colores.RESET)

def mostrar_subtitulo(texto):
    """Muestra un subtítulo formateado."""
    print(Colores.AMARILLO + Colores.NEGRITA + "\n--- " + texto + " ---" + Colores.RESET)

def mostrar_exito(texto):
    """Muestra un mensaje de éxito."""
    print(Colores.VERDE + "✓ " + texto + Colores.RESET)
    time.sleep(1.5)  # Pausa para que el usuario pueda leer el mensaje

def mostrar_error(texto):
    """Muestra un mensaje de error."""
    print(Colores.ROJO + "✗ " + texto + Colores.RESET)
    time.sleep(1.5)  # Pausa para que el usuario pueda leer el mensaje

def mostrar_menu():
    """Muestra el menú de opciones."""
    limpiar_pantalla()
    mostrar_titulo("SISTEMA CRUD DE EMPLEADOS")
    
    print(Colores.CIAN + "1." + Colores.RESET + " Crear Empleado")
    print(Colores.CIAN + "2." + Colores.RESET + " Editar Nombre de Empleado")
    print(Colores.CIAN + "3." + Colores.RESET + " Eliminar Empleado")
    print(Colores.CIAN + "4." + Colores.RESET + " Listar Empleados")
    print(Colores.CIAN + "5." + Colores.RESET + " Salir")
    print("\n" + Colores.NEGRITA + "Seleccione una opción: " + Colores.RESET, end="")

def leer_opcion():
    """Lee y valida la opción ingresada por el usuario."""
    try:
        return int(input())
    except ValueError:
        return 0

def crear_empleado(controller):
    """Solicita datos y crea un nuevo empleado."""
    limpiar_pantalla()
    mostrar_subtitulo("CREAR EMPLEADO")
    
    # Obtener la lista de empleados existentes para verificar IDs
    empleados_existentes = controller.listar_empleados()
    ids_existentes = [emp.identificacion for emp in empleados_existentes]
    
    # Si hay empleados, mostrarlos para referencia
    if empleados_existentes:
        print(Colores.NEGRITA + "\nEmpleados existentes:" + Colores.RESET)
        print(Colores.NEGRITA + "ID\t| NOMBRE" + Colores.RESET)
        print("-" * 40)
        
        for emp in empleados_existentes:
            print(f"{Colores.CIAN}{emp.identificacion}{Colores.RESET}\t| {emp.nombre}")
        
        print("\n")
    
    nombre = input(Colores.NEGRITA + "Ingrese el nombre completo: " + Colores.RESET)
    identificacion = input(Colores.NEGRITA + "Ingrese la identificación: " + Colores.RESET)
    
    # Verificar si el ID ya existe
    if identificacion in ids_existentes:
        mostrar_error(f"La identificación '{identificacion}' ya existe. No se pueden repetir IDs.")
        return
    
    if controller.crear_empleado(nombre, identificacion):
        mostrar_exito("Empleado creado exitosamente.")
    else:
        mostrar_error("Error al crear empleado. Hubo un problema con el archivo.")

def editar_nombre_empleado(controller):
    """Solicita datos y edita el nombre de un empleado."""
    limpiar_pantalla()
    mostrar_subtitulo("EDITAR NOMBRE DE EMPLEADO")
    
    # Mostrar lista de empleados para seleccionar
    empleados = controller.listar_empleados()
    
    if not empleados:
        mostrar_error("No hay empleados registrados.")
        return
    
    print(Colores.NEGRITA + "\nEmpleados disponibles:" + Colores.RESET)
    print(Colores.NEGRITA + "ID\t| NOMBRE" + Colores.RESET)
    print("-" * 40)
    
    for emp in empleados:
        print(f"{Colores.CIAN}{emp.identificacion}{Colores.RESET}\t| {emp.nombre}")
    
    print("\n")
    identificacion = input(Colores.NEGRITA + "Ingrese la identificación del empleado a editar: " + Colores.RESET)
    nuevo_nombre = input(Colores.NEGRITA + "Ingrese el nuevo nombre: " + Colores.RESET)
    
    if controller.editar_nombre_empleado(identificacion, nuevo_nombre):
        mostrar_exito("Nombre de empleado actualizado exitosamente.")
    else:
        mostrar_error("Error al actualizar. El empleado no existe o hubo un problema con el archivo.")

def eliminar_empleado(controller):
    """Solicita identificación y elimina un empleado."""
    limpiar_pantalla()
    mostrar_subtitulo("ELIMINAR EMPLEADO")
    
    # Mostrar lista de empleados para seleccionar
    empleados = controller.listar_empleados()
    
    if not empleados:
        mostrar_error("No hay empleados registrados.")
        return
    
    print(Colores.NEGRITA + "\nEmpleados disponibles:" + Colores.RESET)
    print(Colores.NEGRITA + "ID\t| NOMBRE" + Colores.RESET)
    print("-" * 40)
    
    for emp in empleados:
        print(f"{Colores.ROJO}{emp.identificacion}{Colores.RESET}\t| {emp.nombre}")
    
    print("\n")
    identificacion = input(Colores.NEGRITA + "Ingrese la identificación del empleado a eliminar: " + Colores.RESET)
    
    # Confirmar eliminación
    empleado_a_eliminar = next((emp for emp in empleados if emp.identificacion == identificacion), None)
    if empleado_a_eliminar:
        print(f"\n¿Está seguro que desea eliminar a {Colores.AMARILLO}{empleado_a_eliminar.nombre}{Colores.RESET}? (s/n): ", end="")
        confirmacion = input().lower()
        
        if confirmacion == 's':
            if controller.eliminar_empleado(identificacion):
                mostrar_exito("Empleado eliminado exitosamente.")
            else:
                mostrar_error("Error al eliminar. Hubo un problema con el archivo.")
        else:
            print(Colores.AMARILLO + "\nOperación cancelada." + Colores.RESET)
            time.sleep(1.5)
    else:
        mostrar_error("No existe un empleado con esa identificación.")

def listar_empleados(controller):
    """Lista todos los empleados registrados."""
    limpiar_pantalla()
    mostrar_subtitulo("LISTA DE EMPLEADOS")
    
    empleados = controller.listar_empleados()
    
    if not empleados:
        print(Colores.AMARILLO + "No hay empleados registrados." + Colores.RESET)
        input("\nPresione Enter para continuar...")
        return
    
    # Determinar el ancho máximo para la columna de nombres
    max_nombre_len = max(len(emp.nombre) for emp in empleados) if empleados else 0
    max_id_len = max(len(emp.identificacion) for emp in empleados) if empleados else 0
    
    # Asegurar un ancho mínimo
    max_nombre_len = max(max_nombre_len, 15)
    max_id_len = max(max_id_len, 13)
    
    # Crear encabezados con anchos fijos
    print(Colores.NEGRITA)
    print(f"{'ID'.ljust(max_id_len)} | {'NOMBRE'.ljust(max_nombre_len)}")
    print("-" * (max_id_len + max_nombre_len + 3))
    print(Colores.RESET)
    
    # Mostrar cada empleado con un formato alineado
    for emp in empleados:
        print(f"{Colores.CIAN}{emp.identificacion.ljust(max_id_len)}{Colores.RESET} | {emp.nombre.ljust(max_nombre_len)}")
    
    print("\nTotal de empleados: " + Colores.NEGRITA + str(len(empleados)) + Colores.RESET)
    input("\nPresione Enter para continuar...")

def main():
    """Función principal que maneja el flujo del programa."""
    controller = EmpleadoController()
    salir = False
    
    while not salir:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            crear_empleado(controller)
        elif opcion == 2:
            editar_nombre_empleado(controller)
        elif opcion == 3:
            eliminar_empleado(controller)
        elif opcion == 4:
            listar_empleados(controller)
        elif opcion == 5:
            limpiar_pantalla()
            print(Colores.VERDE + Colores.NEGRITA + "\n¡Hasta pronto!\n" + Colores.RESET)
            salir = True
        else:
            mostrar_error("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()