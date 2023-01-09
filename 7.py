import random
class hashTable():
    def legiones():
        return ['FL', 'TF','TK', 'CT', 'FN', 'FO']
    def hashLegion():
        return lambda e:hashTable.legiones().index(e[0:2])
    def hashCodigo():
        return lambda e:int(e[-3])
    def hashSubLegion():
        return lambda e:hashTable.legiones().index(e)
    def hashSubCodigo():
        return lambda e:int(e)
    def __init__ (self,tam, funcion,funcionSub):
        self.lista = [[] for variable in range(tam)]
        self.hash=funcion
        self.hashSub=funcionSub
    def insertar (self, e):
        self.lista[self.hash(e)].append(e)
    def buscar (self,e):
        return self.lista[self.hash(e)]
    def pertenece(self,e):
        return e in self.lista[self.hash(e)]
    def borrar(self,e):
        return self.lista[self.hash(e)].remove(e)
    def __str__(self) :
        c=""
        for i in self.lista:
            if len(i)!=0:
                c=c+"["
                for j in i:
                    c=c+str(i)+" ,"
                c=c[0:-1]+"],"
        c=c[0:-1]
        return c
    def generarCod():
        c=random.randrange(0,5)
        return hashTable.legiones()[c]+"-"+str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9))
    def subHashTable(self,c):
        return self.lista[self.hashSub(c)]

lista1=hashTable(len(hashTable.legiones()),hashTable.hashLegion(),hashTable.hashSubLegion())
lista2=hashTable(10000,hashTable.hashCodigo(),hashTable.hashSubCodigo())
for i in range(2000):
    c=hashTable.generarCod()
    lista1.insertar(c)
    lista2.insertar(c)
print("Lista_Codigo")
print(str(lista1))
print(str(lista2))
print("borrado")
if lista1.pertenece("FN-2187"):
    lista1.borrar("FN-2187")
    lista2.borrar("FN-2187")
    print("desertor eliminado")
else:
    print("no se encontro el desertor; o esta muerto o se encuentra entre las fuerzas rebeldes")
misionAsalto=lista2.subHashTable(537)
misionExploracion=lista2.subHashTable(781)
DarthVader_Hoth=lista1.subHashTable("CT")
Mision_Exterminacion_Endor=lista1.subHashTable("TF")
print("A continuación se comunica el listado de los soldados que acudirán a las próximas misiones")
print("Mision de asalto: "+str(misionAsalto))
print("Mision de exploracion: "+str(misionExploracion))
print("Mision de exterminacion en Endor: "+str(Mision_Exterminacion_Endor))
print("Custodiar a Lord Vader en Hoth: "+str(DarthVader_Hoth))
