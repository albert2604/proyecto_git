import personas as per
import cancha as can
import reservas as res
class Centro:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = []  
        self.lista_clientes = []
        self.lista_empleados = []
        
        

    @staticmethod
    def main():
        centro = Centro("Centro Deportivo 1", "Arcipreste de Hita")
        while True:
            print("Menú Centro Deportivo:")
            print("1. Crear y agregar cancha")
            print("2. Listar cancha por deporte")
            print("3. Quitar cancha")
            print("4. Crear y agregar cliente")
            print("5. Listar clientes totales")
            print("6. Registrar empleado")
            print("7. Asignar tarea a empleado")
            print("8. Listar empleados desocupados")
            print("9. Quitar empleado")
            print("10. Crear reserva")
            print("11. Listar reservas")
            print("12. Mostrar saldo de un cliente")
            print("13. Salir")
            opcion = input("Escoja una opcion(1-11):")

            match opcion:
                case "1":
                    can.agregar_cancha(centro.lista_canchas)
                case "2":
                    can.listar_canchas_por_deporte(centro.lista_canchas)
                case "3":
                    can.quitar_cancha(centro.lista_canchas)
                case "4":
                    per.agregar_cliente(centro.lista_clientes)
                case "5":
                    per.listar_clientes_totales(centro.lista_clientes)
                case "6":
                    per.registrar_empleado_cancha(centro.lista_canchas)
                case "7":
                    per.asignar_tarea(centro.lista_canchas)
                case "8":
                    per.empleados_desocupados(centro.lista_canchas)
                case "9":
                    per.quitar_empleado_cancha(centro.lista_canchas)
                case "10":
                    res.crear_reserva(centro.lista_canchas, centro.lista_clientes)
                case "11":
                    res.mostrar_reservas(centro.lista_canchas)
                case "12":
                    res.saldo_cliente(centro.lista_clientes)
                case "13":
                    break
                case _:
                    print("Opcion no encontrada, escoja un numero del 1 al 13")
if __name__ == "__main__":
    Centro.main()
