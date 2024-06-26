class Cancha:

    def __init__(self, numero_cancha, deporte,precio, habilitada):
        self.numero_cancha = int(numero_cancha)
        self.deporte = deporte 
        self.precio = int(precio)
        self.habilitada = habilitada
        self.reservas = []
        self.empleados = []
        
    
def crear_cancha():
    numero_cancha = input("numero de la cancha: ")
    deporte = input("Deporte a realizar: ")
    precio = int(input("Precio de la cancha: "))
    habilitada = input("Esta habilitada?: ")
    cancha = Cancha(numero_cancha, deporte, precio, habilitada)
    return cancha

def agregar_cancha(lista_cancha):
    cancha = crear_cancha()
    for c in lista_cancha:
            if c.numero_cancha == cancha.numero_cancha:
                print("Cancha ya en la lista.")
                return

    lista_cancha.append(cancha)
    
    print(f"Cancha {cancha.numero_cancha} agregado exitosamente.")

def listar_canchas_por_deporte(lista_cancha):
    diccionario_canchas = {}
    deporte= input("Que deporte desea buscar?:")
    for cancha in lista_cancha:
        if cancha.deporte.lower() == deporte.lower():
            if deporte not in diccionario_canchas:
                diccionario_canchas[deporte] = []
                diccionario_canchas[deporte].append(cancha)
                print(diccionario_canchas)
        else:
            print("No hay ninguna cacha con ese deporte")

def quitar_cancha(lista_canchas):
    numero = int(input("introduzca el numero de la cancha"))
    for cancha in lista_canchas:
        if cancha.numero_cancha == numero:
            if not cancha.reservas:
                lista_canchas.remove(cancha)
                print("cancha eliminada")
            else:
                print("No se puede quitar la cancha porque tiene resrvas pendientes")
        else:
            print("La cancha no se encontro")





    