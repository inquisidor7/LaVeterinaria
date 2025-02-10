from Persona import ClienteManager, registrar_cliente
from Mascota import Registrar_Mascota
class SistemaVeterinaria:
    def __init__(self):
        self.cliente_manager = ClienteManager()

    def registrar_mascota(self):
        print("🐶 Registrando mascota...")
        mascota = Registrar_Mascota.registrar_mascota(self.cliente_manager)
        if mascota:
            print(f"✅ Mascota {mascota.nombre} registrada correctamente.")

    def programar_cita(self):
        print("📅 Programando cita...")

    def consultar_historial(self):
        print("📋 Consultando historial...")

    def salir(self):
        print("❌ Saliendo del sistema...")
        exit()

    def mostrar_menu(self):
        print("🐾 Bienvenido al sistema de gestión de la veterinaria.")
        print("Seleccione una opción:")
        print("1. 🧑‍💼 Registrar cliente")
        print("2. 🐶 Registrar mascota")
        print("3. 📅 Programar cita")
        print("4. 📋 Consultar historial")
        print("5. ❌ Salir")
    def ejecutar(self):
        opciones = {
            "1": lambda: registrar_cliente(self.cliente_manager),
            "2": self.registrar_mascota,
            "3": self.programar_cita,
            "4": self.consultar_historial,
            "5": self.salir
        }

        while True:
            self.mostrar_menu()
            opcion = input("Ingrese el número de la opción deseada: ")
            if opcion in opciones:
                opciones[opcion]()
            else:
                print("⚠️ Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.ejecutar()
