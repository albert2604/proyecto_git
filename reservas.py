class Reservas:
    reservas_cancha = {}
    reservas_cliente = {}
    def __init__(self, numero_reserva, fecha, cliente, cancha, pago):
        self.numero_reserva = int(numero_reserva)
        self.fecha = fecha
        self. cliente = cliente
        self.cancha = cancha
        self.pago = pago #atributo que almacenará el pago total de todas lass reservas

def crear_reserva(lista_cancha, lista_clientes):
    numero_cancha = int(input("introduzc el numero de la cancha: "))
    id_cliente = input("introduzca id del cliente")
    numero_reserva = int(input("Numero de reserva: "))
    fecha=int(input("introduzca la fecha(ddmmaaaa): "))
    if fecha != 8:
        print("fecha incorrecta")
        return 
    else:
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
                            cliente.saldo -= cancha.precio #restamos el precio de la cancha al saldo del cliente despues de haber verficado si su saldo es correcto
                            reserva.pago += cancha.precio #lo mismo con el atributo de pago una vez pague el cliente sumamos el precio de la cancha al total de pago
                            reserva = Reservas(numero_reserva, fecha, id_cliente, numero_cancha)
                            reserva.reservas_cancha[cancha] = cliente
                            reserva.reservas_cliente[cliente] = cancha
                            return reserva
                        else:
                            print("Saldo de cliente muy bajo, no puede crear la reserva")
                    else:
                        print("Tiene que estar la cancha y el cliente habilitado")
                else:
                    print("id de cliente no encontrado")
        else:
            print("numero de cancha no encontrada")
def mostrar_reservas_cacha(reserva):
    print(reserva.reservas_cancha)

def mostrar_reservas_cliente(reserva):
    print(reserva.reservas_clientes)

def saldo_cliente(lista_clientes):
    id_cliente = input("introduzca el id del cliente que desea ver el saldo: ")
    for cliente in lista_clientes:
        if id_cliente == cliente.id:
            print(f"el saldo de {cliente.nombre} es: {cliente.saldo}")
        else:
            print("cliente no encontrado")







