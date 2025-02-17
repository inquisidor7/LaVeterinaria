
from abc import ABC, abstractmethod
from Persona import ClienteManager, registrar_cliente
class Mascota (ABC):
    def __init__(self, nombre, especie,raza,edad):
        self.id_cliente = None 
        self.nombre=nombre
        self.especie=especie
        self.raza=raza
        self.edad=edad
        self.historia_clinica = []
    

    @abstractmethod
    def agregar(self,detalle):
        pass

class Registrar_Mascota(Mascota):
    def __init__(self, nombre, especie, raza, edad, id_cliente):
        super().__init__(nombre, especie, raza, edad)
        self.id_cliente=id_cliente

    def agregar(self, detalle):
        self.historia_clinica.append(detalle)
    
    def obtener(self):
        return self.historia_clinica
    
    @staticmethod
    def registrar_mascota(cliente_manager):
        try:
            id_cliente=input("ingrese el numero de documento del cliente: ").strip()
            cliente = next((c for c in cliente_manager.clientes if str(c.cc) == id_cliente), None)

            if not cliente:
                print("⚠️ Cliente no encontrado")
                registrar_cliente(cliente_manager),
            nombre_mascota=input("Ingrese el nombre de la mascota: ").strip()
            especie=input("Ingrese la especie: ")
            raza=input("Ingrese la raza: ")
            edad=int(input("Ingrese la edad: ").strip())

            if not nombre_mascota or not especie or not raza or not edad or edad<=0:
                raise ValueError("Uno de los datos ingresados no es valido.")
            
            Registrar_Mascota(nombre_mascota,especie,raza,edad,id_cliente)
            cliente = next((c for c in cliente_manager.clientes if str(c.cc) == id_cliente), None)
            print(f"La macota a sido reguistrada con exito para el cliente {cliente.nombre} ")
            print(f"Mascota: {nombre_mascota}, Especie: {especie}, Raza: {raza}, Edad: {edad}")
        except ValueError as e:
            print (f"⚠️ Error: {e}")


    




    

