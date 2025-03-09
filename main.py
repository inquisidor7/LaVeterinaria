
import datetime

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

class Mascota :
    def __init__(self, id_cliente, nombre, especie,raza,edad):
        self.id_cliente = id_cliente 
        self.nombre=nombre
        self.especie=especie
        self.raza=raza
        self.edad=edad
        self.citas = []

    def programar_cita(self, fecha_hora, motivo):
        cita = Cita(self, fecha_hora, motivo)
        self.citas.append(cita)
        return cita

    def listar_citas(self):
        if not self.citas:
            print(f"📌 No hay citas registradas para {self.nombre}.")
        for i,cita in enumerate(self.citas, 1):
             print(f"{i}. Cita de {cita.motivo} para la fecha {cita.fecha_hora}")

class Cita:
    def __init__(self, mascota, fecha_hora, motivo):
        self.mascota = mascota
        self.fecha_hora = fecha_hora
        self.motivo = motivo

    def __str__(self):
        return f"✅ Cita de {self.mascota.nombre} para {self.fecha_hora} por {self.motivo}"


class ClienteManager:
    def __init__(self):
        self.clientes = []
        self.mascotas_cliente = []
        

    def crear_cliente(self, cc, nombre, contacto, direccion):
        cliente = Cliente(cc, nombre, contacto, direccion)
        self.clientes.append(cliente)
        return cliente

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
    
    def adicionar_mascota(self,cliente, nombre, especie, raza, edad):
        mascota = Mascota(cliente,nombre, especie, raza, edad)
        self.mascotas_cliente.append(mascota)
        return mascota
    
    def buscar_mascota_cliente(self,id_cliente):
        mascotas = [m for m in self.mascotas_cliente if str(m.id_cliente.cc) == id_cliente]
        return mascotas

    

def registrar_cliente():
    cc = input("Ingrese el numero de identificacion del cliente: ")
    while not cc.isdigit():
        print("⚠️ La identificacion no es valida, intente de nuevo.")
        cc = input("Ingrese el numero de identificacion del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    contacto = input("Ingrese el contacto del cliente (10 dígitos): ")
    while True:
        if contacto.isdigit() and len(contacto) == 10:
            contacto = int(contacto)
            break
        else:
            print("⚠️ El contacto debe ser un número de 10 dígitos. Por favor, intente de nuevo.")
            contacto = input("Ingrese el contacto del cliente (10 dígitos): ")
    try:
        cliente = manager.crear_cliente(cc, nombre, contacto, direccion)
        print("✅ Cliente registrado con éxito")
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
        manager.adicionar_mascota(cliente,nombre_mascota, especie, raza, edad)
        print(f"La mascota ha sido registrada con éxito para el cliente {cliente.nombre}")
        print(f"Mascota: {nombre_mascota}, Especie: {especie}, Raza: {raza}, Edad: {edad}")
    except ValueError as e:
        print(f"⚠️ Error: {e}")

def programar_cita():
    id_cliente = input("Ingrese el número de documento del cliente: ").strip()
    cliente = next((c for c in manager.clientes if str(c.cc) == id_cliente), None)
    if not cliente:
        print("⚠️ Cliente no encontrado. Procediendo a registrar cliente.")
        registrar_cliente()
        cliente = manager.clientes[-1]  # Obtenemos el último cliente registrado
    mascotas_cliente = manager.buscar_mascota_cliente(id_cliente)
    if not mascotas_cliente:
        print(f"⚠️ No hay mascotas registradas para {cliente.nombre}. Registre una mascota primero.")
        registrar_mascota()
    mascotas_cliente = manager.buscar_mascota_cliente(id_cliente)
    print("\n🐶 Mascotas disponibles:")
    for i, mascota in enumerate(mascotas_cliente, 1):
        print(f"{i}. {mascota.nombre} ({mascota.especie})")
    try:
        id_mascota = int(input("Indique para que mascota es la cita: "))
        mascota_seleccionada=(mascotas_cliente[id_mascota-1])
    except (IndexError, ValueError):
        print("⚠️ Selección no válida.")
        return
    motivo = input("Ingrese el motivo de la cita: ")
    while True:
        fecha_hora = input("Ingrese la fecha y hora de la cita (Año-Mes-Dia Hora:Minuto): ")
        try:
            fecha_hora = datetime.datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("⚠️ Formato incorrecto. Por favor, ingrese la fecha y hora en el formato 'Año-Mes-Dia Hora:Minuto'.")
    cita = mascota_seleccionada.programar_cita(fecha_hora,motivo)
    print("✅ Cita programada con éxito.")
    print(cita)

def consultar_historial():
    print("📋 Consultando historial...")
    id_cliente = input("Ingrese el número de documento del cliente: ").strip()
    cliente = next((c for c in manager.clientes if str(c.cc) == id_cliente), None)
    if not cliente:
        print("⚠️ Cliente no encontrado. Procediendo a registrar cliente.")
        registrar_cliente()
        cliente = manager.clientes[-1]  # Obtenemos el último cliente registrado
    mascotas_cliente = manager.buscar_mascota_cliente(id_cliente)
    if not mascotas_cliente:
        print(f"⚠️ No hay mascotas registradas para {cliente.nombre}.")
        return
    print("\n🐶 Mascotas disponibles:")
    for i, mascota in enumerate(mascotas_cliente, 1):
        print(f"{i}. {mascota.nombre} ({mascota.especie})")
    try:
        id_mascota = int(input("Indique el número de la mascota: ")) - 1
        mascota_seleccionada = mascotas_cliente[id_mascota]
    except (IndexError, ValueError):
        print("⚠️ Selección no válida.")
        return
    
    print(f"\n📜 Historial de citas para {mascota_seleccionada.nombre}:")
    mascota_seleccionada.listar_citas()

def salir():
    print("❌ Sistema finalizado")
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