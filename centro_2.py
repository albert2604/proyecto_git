import cancha as can
import reservas as res
import personas as per

class Centro:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = []  
        self.lista_clientes = []

    @staticmethod
    def main():
        centro = Centro("Centro Deportivo 1", "Arcipreste de Hita")
        while True:
            print("\nMenú Centro Deportivo:")
            print("1. Crear y agregar cancha")
            print("2. Listar canchas por deporte")
            print("3. Quitar cancha")
            print("4. Crear y agregar cliente")
            print("5. Listar clientes")
            print("6. Registrar empleado en cancha")
            print("7. Asignar tarea a empleado")
            print("8. Listar empleados desocupados")
            print("9. Salir")
            opcion = input("Escoja una opción (1-9): ")

            if opcion == "1":
                can.agregar_cancha

            elif opcion == "2":
                if not centro.lista_canchas:
                    print("No hay canchas disponibles para agregar.")
                else:
                    can.agregar_cancha(centro.lista_canchas[-1], centro.lista_canchas)

            elif opcion == "1":
                can.listar_canchas_por_deporte(centro.lista_canchas)

            elif opcion == "2":
                can.quitar_cancha(centro.lista_canchas)

            elif opcion == "3":
                cliente = per.crear_cliente()
                centro.lista_clientes.append(cliente)
                print("Cliente creado y agregado al centro.")

            elif opcion == "4":
                if not centro.lista_clientes:
                    print("No hay clientes disponibles para agregar.")
                else:
                    per.agregar_cliente(centro.lista_clientes)

            elif opcion == "5":
                per.listar_clientes_totales(centro.lista_clientes)

            elif opcion == "6":
                per.registrar_empleado_cancha(centro.lista_canchas, cancha.lista_empleados)

            elif opcion == "7":
                per.asignar_tarea(cancha.lista_empleados)

            elif opcion == "8":
                per.empleados_desocupados(cancha.lista_empleados)

            elif opcion == "9":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 11.")

if __name__ == "__main__":
    Centro.main()