"""Creamos la clase persona y la clase heredada Cliente
    """
class Personas:
    def __init__(self, nombre, apellido) :
        self.nombre = nombre
        self.apellido = apellido
        
class Clientes(Personas):
    def __init__(self, id, nombre, apellido, telefono, activo, saldo ):
        super().__init__(nombre, apellido)
        self.id = id       
        self.telefono = telefono
        self.activo = activo
        
        self.saldo = saldo


"""Funciones para crear y registrar al cliente"""    


def crear_cliente():
    id = input("Ingrese el ID del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    saldo = int(input("dime el saldo que quieres ingresar"))
    activo_input = input("¿El cliente está activo? (s/n): ")
    activo = activo_input.lower() == 's'
    
    cliente = Clientes(id, nombre, apellido, telefono, activo, saldo)
    return cliente


    
def agregar_cliente(lista_clientes):

    cliente = crear_cliente()

    # Verificar si el cliente ya está en la lista
    for c in lista_clientes:
        if c.id == cliente.id:
            print("Cliente ya en la lista.")
            return

    # Agregar el nuevo cliente a la lista
    lista_clientes.append(cliente)
    print(f"Cliente {cliente.nombre} {cliente.apellido} agregado exitosamente.")


    """Funcion quitar cliente de la lista que nos solicite el usuario
    """

def quitar_cliente(lista_clientes):
    id = input("Ingrese el ID del cliente que desea eliminar: ")
    
    # Buscar el cliente por ID y eliminarlo si existe
    for cliente in lista_clientes:
        if cliente.id == id:
            lista_clientes.remove(cliente)
            print(f"Cliente {cliente.nombre} {cliente.apellido} eliminado exitosamente.")
            return
    
    # Si no se encuentra el cliente con el ID proporcionado
    print("Cliente no encontrado.")
    
"""Funcion para mostrar la lista de clientes totales"""

def listar_clientes_totales(lista_clientes):
    if not lista_clientes:
        print("No hay clientes en la lista.")
    else:
        print("Lista de clientes:")
        for cliente in lista_clientes:
            if cliente.activo : 
                estado = "Activo" 
            else:
                estado = "Inactivo"
            print(f"ID: {cliente.id}, Nombre: {cliente.nombre} {cliente.apellido}, Teléfono: {cliente.telefono}, Estado: {estado}")


    """Creamos la clase empleados heredada de la clase personas
    """


class Empleados(Personas):
    def __init__(self, id, nombre, apellido):
        super().__init__(nombre, apellido)
        self.id = id
        self.desocupado = True
        self.tareas = []

        """Funcion para registrar empleados en una cancha,
        solicitando el id del empleado y la cancha en la que se quiere registrar.
        """

def crear_empleado():
    id_empleado = input("Ingrese el ID del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    return Empleados(id_empleado, nombre, apellido)


def registrar_empleado_cancha(lista_canchas, lista_empleados):
    empleado = crear_empleado()

    # Verificar si el empleado ya está registrado en alguna cancha
    for cancha in lista_canchas:
        if empleado_encontrado in cancha.empleados:
            print(f"El empleado {empleado_encontrado.nombre} {empleado_encontrado.apellido} ya está registrado en otra cancha.")
            return

    # Solicitar al usuario que ingrese el deporte de la cancha que desea utilizar
    deporte_cancha = input("Ingrese el deporte de la cancha que desea utilizar: ")

    # Buscar la cancha por su deporte
    canchas_deporte = []
    for c in lista_canchas:
        if c.deporte.lower() == deporte_cancha.lower():
            canchas_deporte.append(c)
        if not canchas_deporte:
            print("No hay ninguna cancha disponible para el deporte especificado.")
        return

    print("Canchas disponibles para el deporte especificado:")
    for i, cancha in enumerate(canchas_deporte):
        print(f"{i}: Cancha {cancha.numero_cancha}")

    opcion_cancha = int(input("Seleccione el número de la cancha: ")) 

    if opcion_cancha < 0 or opcion_cancha >= len(canchas_deporte):
        print("Opción inválida.")
        return

    cancha_seleccionada = canchas_deporte[opcion_cancha]

    if cancha_seleccionada.habilitada.lower() != "si":
        print(f"La cancha {cancha_seleccionada.numero_cancha} no está habilitada.")
        return

    # Registrar al empleado en la cancha
    cancha_seleccionada.empleados.append(empleado)
    cancha_seleccionada.habilitada = "no"
    print(f"Empleado {empleado.nombre} {empleado.apellido} registrado en la cancha {cancha_seleccionada.numero_cancha}.")

    # Agregar el empleado a la lista de empleados
    lista_empleados.append(empleado)
    """Funcion para asignar una tarea a un empleado 
    """
def asignar_tarea(lista_canchas):
    id_empleado = input("Ingrese el ID del empleado al que desea asignar la tarea: ")
    tarea = input("Ingrese la tarea que desea asignar: ")

    for cancha in lista_canchas:
        for empleado in cancha.empleados:
            if empleado.id == id_empleado:
                if empleado.desocupado:
                    empleado.tareas.append(tarea)
                    empleado.desocupado = False
                    print(f"Tarea '{tarea}' asignada al empleado {empleado.nombre} {empleado.apellido}.")
                else:
                    print(f"El empleado {empleado.nombre} {empleado.apellido} ya tiene tareas asignadas.")
                return
        print("Empleado no encontrado.")

"""
Funcion para mostrar la lista de todos los empleados desocupados en ese momento.
"""
#Mostrar empleados desocupados
def empleados_desocupados(lista_canchas):
    desocupados = []
    for cancha in lista_canchas:
        for empleado in cancha.empleados:
            if empleado.desocupado:
                desocupados.append(empleado)
        
        if not desocupados:
            print("No hay empleados desocupados.")
        else:
            print("Empleados desocupados:")
            for empleado in desocupados:
                print(f"ID: {empleado.id}, Nombre: {empleado.nombre} {empleado.apellido}")
""" 
    Funcion para quitar empleados de la cancha 
"""
#Quitar un empleado de la cancha
def quitar_empleado_cancha(lista_canchas):
    id_empleado = input("Ingrese el ID del empleado que desea quitar de la cancha: ")
    
    for cancha in lista_canchas:
        for empleado in cancha.empleados:
            if empleado.id == id_empleado:
                cancha.empleados.remove(empleado)
                empleado.desocupado = True
                print(f"Empleado {empleado.nombre} {empleado.apellido} quitado de la cancha {cancha.numero_cancha}.")
                return
    print("Empleado no encontrado en ninguna cancha.")
