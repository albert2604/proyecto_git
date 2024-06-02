class Cancha:

    def __init__(self, numero_cancha, deporte,precio, habilitada):
        self.numero_cancha = int(numero_cancha)
        self.deporte = deporte 
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []
        self.empleados = []
        
    
def crear_cancha(canchas):
    numero_cancha = int(input("numero de la cancha: "))
    deporte = input("Deporte a realizar: ")
    precio = input("Precio de la cancha: ")
    habilitada = input("Esta habilitada?: ")
    cancha = Cancha(numero_cancha, deporte, precio, habilitada)
    canchas.append(cancha)
    return cancha
def agregar_cancha(canchas, lista_cancha):
    numero = int(input("Introduce el numero de cancha: "))
    for cancha in canchas:
        if cancha.numero_cancha == numero:
            if cancha in lista_cancha:
                print(f"La cancha {cancha.numero_cancha} ya esta agregada")
            else:
                lista_cancha.append(cancha)
        
def listar_canchas_por_deporte(cancha, lista_cancha):
    diccionario_canchas = {}
    deporte= input("Que deporte desea buscar?:")
    for cancha in lista_cancha:
        if cancha.deporte.lower() == deporte.lower():
            if deporte not in diccionario_canchas:
                diccionario_canchas[deporte] = []
                diccionario_canchas[deporte].append(cancha)
        else:
            print("No hay ninguna cacha con ese deporte")

def quitar_cancha(lista_canchas):
    numero = int(input("introduzca el numero de la cancha"))
    for cancha in lista_canchas:
        if cancha.numero_cancha == numero:
            if not cancha.reservas:
                lista_canchas.remove(cancha)
            else:
                print("No se puede quitar la cancha porque tiene resrvas pendientes")
        else:
            print("La cancha no se encontro")





    