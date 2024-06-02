class Reservas:
    
    def __init__(self, numero_reserva, fecha, cliente, cancha, pago):
        self.numero_reserva = int(numero_reserva)
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
        self.pago = int(pago) #atributo que almacenará el pago total de todas lass reservas

def crear_reserva(lista_cancha, lista_clientes):
    numero_cancha = int(input("introduzca el numero de la cancha: "))
    id_cliente = input("introduzca id del cliente: ")
    numero_reserva = int(input("Numero de reserva: "))
    fecha = int(input("introduzca la fecha (ddmmaaaa): "))
    pago = int (input("cuanto quieres ingresar?: "))
    dia = fecha // 1000000
    mes = (fecha // 10000) % 100
    anio = fecha % 10000
    fecha_formateada = (dia, mes, anio)

    for cancha in lista_cancha:
        if numero_cancha == cancha.numero_cancha:
            for cliente in lista_clientes:
                if id_cliente == cliente.id:
                    cliente.saldo += pago
                    if cancha.habilitada.lower() == "si":
                        if cliente.saldo >= -2000:
                            cliente.saldo -= cancha.precio
                            reserva = Reservas(numero_reserva, fecha_formateada, cliente.id, cancha.numero_cancha, pago)
                            cancha.reservas.append(reserva)
                            print("Reserva completada")
                            return reserva
                        else:
                            print("Saldo de cliente muy bajo, no puede crear la reserva")
                    else:
                        print("Tiene que estar la cancha y el cliente habilitado")
                else:
                    print("id de cliente no encontrado")
        else:
            print("numero de cancha no encontrada")
def mostrar_reservas(lista_cancha):
    for cancha in lista_cancha:
        for reservas in cancha.reservas:
            print(f"la reservas de la cancha {reservas.cancha} son: nº reserva:{reservas.numero_reserva},\nfecha:{reservas.fecha},\nid del cliente:{reservas.cliente}\n")
            print(f"la reservas del cliente {reservas.cliente} son:  nº reserva:{reservas.numero_reserva},\nfecha:{reservas.fecha},\nNº de cancha:{reservas.cancha}\n")

def saldo_cliente(lista_clientes):
    id_cliente = input("introduzca el id del cliente que desea ver el saldo: ")
    for cliente in lista_clientes:
        if id_cliente == cliente.id:
            print(f"el saldo de {cliente.nombre} es: {cliente.saldo}")
        else:
            print("cliente no encontrado")







