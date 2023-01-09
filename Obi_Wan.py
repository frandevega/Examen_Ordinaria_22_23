class mochila ():
    def __init__ (self ):
        self.objetos = []
    def __str__ (self):
        return str(self.objetos)
    def __len__ (self):
        return len(self.objetos)
    def usar_fuerza (self, i=0):
        if i == len(self.objetos):
            return "No hay sable en la mochila"
        elif self.objetos[i] == "sable":
            return "El sable está en la posición " + str(i+1) + " de la mochila"
        else:
            return self.usar_fuerza(i+1)
    def agregar_objeto (self, objeto):
        self.objetos.append(objeto)
    def sacar_objeto (self, i=0):
        if i==len(self.objetos):
            return "No hay objetos en la mochila"
        else:
            a=self.objetos.pop(i)
            return "El objeto " + str(a) + " fue sacado de la mochila"
            
    

mochila_Obi_Wan = mochila()
mochila_Obi_Wan.agregar_objeto("blaster")
mochila_Obi_Wan.agregar_objeto("manzana")
mochila_Obi_Wan.agregar_objeto("sable")
print(mochila_Obi_Wan)
print(mochila_Obi_Wan.sacar_objeto())
print(mochila_Obi_Wan)
print(mochila_Obi_Wan.usar_fuerza())