class stormtrooper:
    def __init__(self, nombre,rango):
        self.nombre = nombre
        self.rango = rango
        print("Stormtrooper creado")
    def __str__(self):
        return self.nombre + " " + self.rango

a=stormtrooper("TK","8654")
b=stormtrooper("FN","8654")
lista=[a,b]
for i in lista:
    print(i)