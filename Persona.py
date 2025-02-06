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
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
    
    def __str__(self):
        return f"Cliente: {self.nombre}, Contacto: {self.contacto}, Dirección: {self.direccion}"

class ClienteManager:
    def __init__(self):
        self.clientes = []
    
    def crear_cliente(self, nombre, contacto, direccion):
        cliente = Cliente(nombre, contacto, direccion)
        self.clientes.append(cliente)
        return cliente

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

def registrar_cliente(manager):
    nombre = input("Ingrese el nombre del cliente: ")
    contacto = int(input("Ingrese el contacto del cliente (10 dígitos): "))
    direccion = input("Ingrese la dirección del cliente: ")
    try:
        cliente = manager.crear_cliente(nombre, contacto, direccion)
        print("Cliente registrado con éxito:")
        print(cliente)
    except ValueError as e:
        print(f"Error: {e}")

def registrar_mascota():
    print("Función registrar_mascota aún no implementada.")

def programar_cita():
    print("Función programar_cita aún no implementada.")

def consultar_historial():
    print("Función consultar_historial aún no implementada.")

def salir():
    print("Saliendo del sistema.")

def menu():
    opciones = {
        "1": lambda: registrar_cliente(manager),
        "2": registrar_mascota,
        "3": programar_cita,
        "4": consultar_historial,
        "5": salir
    }
    while True:
        print("\nMenú:")
        print("1. Registrar Cliente")
        print("2. Registrar Mascota")
        print("3. Programar Cita")
        print("4. Consultar Historial")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida, intente de nuevo.")

# Inicializar manager y ejecutar el menú
manager = ClienteManager()
menu()
