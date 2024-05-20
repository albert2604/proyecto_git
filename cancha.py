class Cancha:

    def __init__(self, numero_cancha, deporte,precio, habilitada):
        self.numero_cancha = numero_cancha
        self.deporte = deporte 
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []
        self.empleados = []
        self.canchas = {}

    def crear_cancha(self):
        numero_cancha = input("numero de la cancha: ")
        deporte = input("Deporte a realizar: ")
        precio = input("Precio de la cancha: ")
        habilitada = input("Esta habilitada?: ")
        cancha = Cancha(numero_cancha, deporte, precio, habilitada)
        self.canchas[numero_cancha] = {"deporte": deporte, "precio": precio, "habilitada": habilitada}

    def agregar_cancha(self):
       numero_cancha = input("numero de la cancha: ")
       if numero_cancha in self.canchas:
           pass
       

