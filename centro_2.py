import personas as per
import cancha as can
import reservas as res
class Centro:
    def _init_(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = []  
        self.lista_clientes = []
        self.lista_empleados = []
        
        

    @staticmethod
    def main():
        centro = Centro("Centro Deportivo 2", "Arcipreste de Hita")
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
            

            opcion = input("Escoja una opcion(1-13):")

            if opcion == "1":
                pass
            elif opcion == "2":
                can.listar_canchas_por_deporte(centro.lista_canchas)
            elif opcion == "3":
                can.quitar_cancha(centro.lista_canchas)
            elif opcion == "4":
                per.agregar_cliente(centro.lista_clientes)
            elif opcion == "5":
                per.listar_clientes_totales(centro.lista_clientes)
            elif opcion == "6":
                per.registrar_empleado_cancha(centro.lista_canchas, centro.lista_empleados)
            elif opcion == "7":
                per.asignar_tarea(centro.lista_empleados)
            elif opcion == "8":
                per.empleados_desocupados(centro.lista_empleados)
            elif opcion == "9":
                per.quitar_empleado_cancha(centro.lista_empleados, centro.lista_canchas)
            elif opcion == "10":
                res.crear_reserva(centro.lista_canchas, centro.lista_clientes)
            elif opcion == "11":
                # Aquí necesitaríamos una función para mostrar reservas de una cancha específica o del cliente
                pass
            elif opcion == "12":
                res.saldo_cliente(centro.lista_clientes)
            elif opcion == "13":
                pass
            else:
                print("Opcion no encontrada, escoja un numero del 1 al 13")
if __name__ == "__main__":
    Centro.main()