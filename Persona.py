class Persona:
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.set_contacto(contacto)
        self.direccion = direccion

    def set_contacto(self, contacto):
        if isinstance(contacto, int) and len(str(contacto)) == 10:
            self.contacto = contacto
        else:
            raise ValueError("El contacto debe ser un número de 10 dígitos.")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Contacto: {self.contacto}")
        print(f"Dirección: {self.direccion}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Contacto: {self.contacto}, Dirección: {self.direccion}"


class Cliente(Persona):
    def __init__(self, cc, nombre, contacto, direccion):
        self.cc = cc
        super().__init__(nombre, contacto, direccion)

    def __str__(self):
        return f"Cliente: {self.cc}, {self.nombre}, Contacto: {self.contacto}, Dirección: {self.direccion}"


class ClienteManager:
    def __init__(self):
        self.clientes = []

    def crear_cliente(self, cc, nombre, contacto, direccion):
        cliente = Cliente(cc, nombre, contacto, direccion)
        self.clientes.append(cliente)
        return cliente

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)


def registrar_cliente():
    cc = int(input("Ingrese el numero de identificacion del cliente: "))
    nombre = input("Ingrese el nombre del cliente: ")
    while True:
        contacto = input("Ingrese el contacto del cliente (10 dígitos): ")
        if contacto.isdigit() and len(contacto) == 10:
            contacto = int(contacto)
            break
        else:
            print("⚠️ El contacto debe ser un número de 10 dígitos. Por favor, intente de nuevo.")
    direccion = input("Ingrese la dirección del cliente: ")
    try:
        cliente = manager.crear_cliente(cc, nombre, contacto, direccion)
        print("✅ Cliente registrado con éxito:")
        print(cliente)
    except ValueError as e:
        print(f"Error: {e}")


def registrar_mascota():
    try:
        id_cliente = input("Ingrese el número de documento del cliente: ").strip()
        cliente = next((c for c in manager.clientes if str(c.cc) == id_cliente), None)

        if not cliente:
            print("⚠️ Cliente no encontrado. Procediendo a registrar cliente.")
            registrar_cliente()
            cliente = manager.clientes[-1]  # Obtenemos el último cliente registrado

        nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
        especie = input("Ingrese la especie: ")
        raza = input("Ingrese la raza: ")
        edad = int(input("Ingrese la edad: ").strip())

        if not nombre_mascota or not especie or not raza or edad <= 0:
            raise ValueError("Uno de los datos ingresados no es válido.")

        print(f"La mascota ha sido registrada con éxito para el cliente {cliente.nombre}")
        print(f"Mascota: {nombre_mascota}, Especie: {especie}, Raza: {raza}, Edad: {edad}")
    except ValueError as e:
        print(f"⚠️ Error: {e}")


def programar_cita():
    print("📅 Programando cita...")


def consultar_historial():
    print("📋 Consultando historial...")


def salir():
    print("❌ Sistema Finalizado")
    exit()

def mostrar_menu():
    print("🐾 Bienvenido al sistema de gestión de la veterinaria.")
    print("Seleccione una opción:")
    print("1. 🧑‍💼 Registrar cliente")
    print("2. 🐶 Registrar mascota")
    print("3. 📅 Programar cita")
    print("4. 📋 Consultar historial")
    print("5. ❌ Salir")


opciones = {
    "1": registrar_cliente,
    "2": registrar_mascota,
    "3": programar_cita,
    "4": consultar_historial,
    "5": salir
}

# Inicializar manager
manager = ClienteManager()

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    if opcion in opciones:
        opciones[opcion]()
    else:
        print("⚠️ Opción no válida, por favor intente de nuevo.")