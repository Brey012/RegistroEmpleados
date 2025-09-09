# Lista para almacenar a los empleados. Cada empleado será un diccionario.
empleados = []
# Variable para asignar un ID único y autoincremental a cada empleado.
next_id = 1

def registrar_empleado():
    """
    Registra un nuevo empleado pidiendo los datos por consola
    y lo añade a la lista 'empleados'.
    """
    global next_id # Usamos la variable global para el ID
    print("\n--- Registro de Nuevo Empleado ---")
    
    # Pedir datos del empleado
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    telefono = input("Teléfono: ")
    cargo = input("Cargo: ")
    
    # Validar que el valor por hora y las horas sean números
    while True:
        try:
            valor_hora = float(input("Valor por hora: "))
            horas_trabajadas = int(input("Horas trabajadas en el mes: "))
            break # Si son números válidos, salimos del bucle
        except ValueError:
            print("Error: El valor por hora y las horas deben ser números. Inténtalo de nuevo.")

    # Crear el diccionario del empleado
    empleado = {
        'id': next_id,
        'nombre': nombre,
        'correo': correo,
        'telefono': telefono,
        'cargo': cargo,
        'valor_hora': valor_hora,
        'horas_trabajadas': horas_trabajadas
    }
    
    # Añadir el empleado a la lista y aumentar el ID para el siguiente
    empleados.append(empleado)
    next_id += 1
    
    print(f"\n✅ Empleado '{nombre}' registrado con éxito con el ID: {empleado['id']}")

def ver_todos_los_empleados():
    """
    Muestra una lista con todos los empleados registrados,
    su cargo y su salario calculado.
    """
    print("\n--- Lista de Todos los Empleados ---")
    if not empleados:
        print("No hay empleados registrados.")
        return
        
    for emp in empleados:
        salario = emp['horas_trabajadas'] * emp['valor_hora']
        print(f"ID: {emp['id']} | Nombre: {emp['nombre']} | Cargo: {emp['cargo']} | Salario: ${salario:,.2f}")

def ver_total_nomina():
    """
    Calcula y muestra el costo total de la nómina (la suma de
    los salarios de todos los empleados).
    """
    print("\n--- Total de la Nómina ---")
    if not empleados:
        print("No hay empleados registrados para calcular la nómina.")
        return
        
    total_nomina = 0
    for emp in empleados:
        salario = emp['horas_trabajadas'] * emp['valor_hora']
        total_nomina += salario
        
    print(f"El costo total de la nómina es: ${total_nomina:,.2f}")

def eliminar_empleado_por_id():
    """
    Pide un ID y elimina al empleado correspondiente de la lista.
    """
    print("\n--- Eliminar Empleado por ID ---")
    if not empleados:
        print("No hay empleados para eliminar.")
        return
        
    try:
        id_a_eliminar = int(input("Introduce el ID del empleado que deseas eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    empleado_encontrado = None
    for emp in empleados:
        if emp['id'] == id_a_eliminar:
            empleado_encontrado = emp
            break
            
    if empleado_encontrado:
        empleados.remove(empleado_encontrado)
        print(f"✅ Empleado '{empleado_encontrado['nombre']}' (ID: {id_a_eliminar}) ha sido eliminado.")
    else:
        print(f"❌ No se encontró ningún empleado con el ID {id_a_eliminar}.")

def main():
    """
    Función principal que muestra el menú y gestiona las opciones del usuario.
    """
    while True:
        print("\n=====================================")
        print("   Sistema de Gestión de Nómina   ")
        print("=====================================")
        print("1. Registrar Empleado")
        print("2. Ver todos los empleados")
        print("3. Ver el total de la Nómina")
        print("4. Eliminar Empleado por ID")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            registrar_empleado()
        elif opcion == '2':
            ver_todos_los_empleados()
        elif opcion == '3':
            ver_total_nomina()
        elif opcion == '4':
            eliminar_empleado_por_id()
        elif opcion == '5':
            print("\n👋 ¡Hasta luego! Saliendo del programa.")
            break
        else:
            print("\n❌ Opción no válida. Por favor, elige un número del 1 al 5.")

# Iniciar el programa
if __name__ == "__main__":
    main()