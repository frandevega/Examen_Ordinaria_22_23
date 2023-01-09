

class artefacto_valioso:
    def __init__(self,nombre,peso,fecha_caducidad):
        self.nombre = nombre
        self.peso = peso
        self.fecha_caducidad = fecha_caducidad
        print("Artefacto creado")
    def __str__(self):
        return self.nombre + " " + self.peso + " " + self.fecha_caducidad
    def crearArtefacto():
        return artefacto_valioso(input("Nombre: "),input("Peso: "),input("Fecha de caducidad: "))
    def crearLista():
        lista=[]
        for i in range(3):
            lista.append(artefacto_valioso.crearArtefacto())
        return lista
    def ordenar(lista):
        lista.sort(key=lambda x:x.fecha_caducidad)
        return lista
    def modificar(lista):
        lista[0].nombre=input("Nuevo_nombre: ")
        return lista
lista=artefacto_valioso.crearLista()
print(artefacto_valioso.ordenar(lista=lista))
print(artefacto_valioso.modificar(lista=lista))