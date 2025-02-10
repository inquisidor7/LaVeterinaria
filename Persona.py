class Persona:
    def __init__(self,cc, nombre, contacto, direccion):
        self.cc = cc
        self.nombre = nombre
        self.set_contacto(contacto)
        self.direccion = direccion

    def set_contacto(self, contacto):
        if isinstance(contacto, int) and len(str(contacto)) == 10:
            self.contacto = contacto
        else:
            raise ValueError("⚠️ El contacto debe ser un número de 10 dígitos.")

    def mostrar_informacion(self):
        print(f"CC: {self.cc}")
        print(f"Nombre: {self.nombre}")
        print(f"Contacto: {self.contacto}")
        print(f"Dirección: {self.direccion}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Contacto: {self.contacto}, Dirección: {self.direccion}"

class Cliente(Persona):
    def __init__(self,cc, nombre, contacto, direccion):
        super().__init__(cc,nombre, contacto, direccion)
    
    def __str__(self):
        return f"Cliente: {self.nombre}, Contacto: {self.contacto}, Dirección: {self.direccion}"

class ClienteManager:
    def __init__(self):
        self.clientes = []
    
    def crear_cliente(self,cc, nombre, contacto, direccion):
        cliente = Cliente(cc,nombre, contacto, direccion)
        self.clientes.append(cliente)
        return cliente

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

def registrar_cliente(manager):
    cc = int(input("Ingrese el cnumero de identificacion del cliente (10 dígitos): "))
    nombre = input("Ingrese el nombre del cliente: ")
    contacto = int(input("Ingrese el contacto del cliente (10 dígitos): "))
    direccion = input("Ingrese la dirección del cliente: ")
    try:
        cliente = manager.crear_cliente(cc,nombre, contacto, direccion)
        print("Cliente registrado con éxito:")
        print(cliente)
    except ValueError as e:
        print(f"⚠️ Error: {e}")
