def mostrar_menu():
    print("🐾 Bienvenido al sistema de gestión de la veterinaria.")
    print("Seleccione una opción:")
    print("1. \U0001F9D1\U0000200D\U0001F4BC Registrar cliente")
    print("2. \U0001F436 Registrar mascota")
    print("3. \U0001F4C5 Programar cita")
    print("4. \U0001F4CB Consultar historial")
    print("5. \U0000274C Salir")

def registrar_cliente():
    print("🧑‍💼 Registrando cliente...")

def registrar_mascota():
    print("🐶 Registrando mascota...")

def programar_cita():
    print("📅 Programando cita...")

def consultar_historial():
    print("📋 Consultando historial...")

def salir():
    print("❌ Saliendo del sistema...")
    exit()

opciones = {
    "1": registrar_cliente,
    "2": registrar_mascota,
    "3": programar_cita,
    "4": consultar_historial,
    "5": salir
}

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion in opciones:
        opciones[opcion]()
    else:
        print("⚠️ Opción no válida, por favor intente de nuevo.")
