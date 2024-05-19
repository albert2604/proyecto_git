lista_clientes = []
lista_empleados = []
class Personas:
    def __init__(self, nombre, apellido) :
        self.nombre = nombre
        self.apellido = apellido
        
class Clientes(Personas):
    def __init__(self, id, nombre, apellido, telefono, activo ):
        super().__init__(nombre, apellido)
        self.id = id       
        self.telefono = telefono
        self.activo = activo
    
def crear_cliente():
    id = input("Ingrese el ID del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    activo_input = input("¿El cliente está activo? (s/n): ")
    activo = activo_input.lower() == 's'
    
    nuevo_cliente = Clientes(id, nombre, apellido, telefono, activo)
    return nuevo_cliente


    
def agregar_cliente(cliente):

    nuevo_cliente = crear_cliente()

    
    for c in lista_clientes:
        if c.id == cliente.id:
            print("Cliente ya en la lista.")
            return

    
    lista_clientes.append(cliente)
    
def quitar_cliente():
    id = input("Ingrese el ID del cliente que desea eliminar: ")
    
    
    for cliente in lista_clientes:
        if cliente.id == id:
            lista_clientes.remove(cliente)
            print(f"Cliente {cliente.nombre} {cliente.apellido} eliminado.")
            return
    
    
    print("Cliente no encontrado.")
    
def listar_clientes_morosos():
    pass



class Empleados(Personas):
    def __init__(self, nombre, apellido, desocupado, tareas):
        super().__init__(nombre, apellido)
        self.desocupado = desocupado
        self.tareas = tareas


def registrar_empleado():
    id = input("dime el id: ")
    if id in lista_clientes:

        pass
def asignar_tarea():
    pass

def empleados_desocupados():
    pass

def quitar_empleado():
    id = input("dime el id del empleado: ")
    for empleado in lista_empleados:
        if empleado.id in lista_empleados:
            lista_empleados.remove(empleado)
            print(f"{empleado.nombre} {empleado.apellido} eliminado")


