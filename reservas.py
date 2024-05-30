class Reservas:
    def __init__(self, numero_reserva, fecha, cliente, cancha):
        self.numero_reserva = int(numero_reserva)
        self.fecha = fecha
        self. cliente = cliente
        self.cancha = cancha

def crear_reserva(lista_cancha, lista_clientes):
    numero_cancha = int(input("introduzc el numero de la cancha: "))
    id_cliente = input("introduzca id del cliente")
    numero_reserva = int(input("Numero de reserva: "))
    fecha=int(input("introduzca la fecha(ddmmaaaa): "))
    dia= fecha // 1000000
    mes= (fecha // 10000) % 100
    anio= fecha % 10000
    fecha = [(dia, mes, anio)]

    for cancha in lista_cancha:
        if numero_cancha == cancha.numero_cancha:
            for cliente in lista_clientes:
                if id_cliente == cliente.id:
                    if cancha.habilatado == "si" and cliente.activo == "s":
                        if cliente.saldo >= -2000:
                            cliente.saldo -= cancha.precio
                            reserva = Reservas(numero_reserva, fecha, id_cliente, numero_cancha)
                            return reserva
                        else:
                            print("Saldo de cliente muy bajo, no puede crear la reserva")
                    else:
                        print("Tiene que estar la cancha y el cliente habilitado")
                else:
                    print("id de cliente no encontrado")
        else:
            print("numero de cancha no encontrada")



