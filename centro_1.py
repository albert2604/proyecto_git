import personas as per
import cancha as can
import reservas as res
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
            print("Menú Centro Deportivo:")
            print("1. Crear cancha")
            print("2. Agregar cancha/s")
            print("3. Listar cancha por deporte")
            print("4. Quitar cancha")
            print("5. Crear cliente")
            print("6. Agregar cliente")
            print("7. Listar cliente")
            print("8. Registrar empleado")
            print("9. Asignar tarea a empleado")
            print("10. Listar empleados desocupados")
            print("11. Salir")
            opcion = input("Escoja una opcion(1-11):")

            match opcion:
                case "1":
                    cancha = can.crear_cancha(centro.lista_canchas)
                case "2":
                    can.agregar_cancha(cancha, centro.lista_canchas)
                    print(centro.lista_canchas)
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    pass
                case "8":
                    pass
                case "9":
                    pass
                case "10":
                    pass
                case "11":
                    break
                case _:
                    print("Opcion no encontrada, escoja un numero del 1 al 11")
if __name__ == "__main__":
    Centro.main()
