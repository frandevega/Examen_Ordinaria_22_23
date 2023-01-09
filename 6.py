def mochila_Cassian_Andor(objetos, capacidad):

    def Cassian_Andor(i, peso, valor_alcanzable, mochila):
        # Si hemos recorrido todos los objetos, guardamos la solución
        global valor_optimo
        global mochila_opt    
        if i == n:
            mochila_opt = mochila[:]
            valor_optimo = valor_alcanzable
        else:
            # Soluciones añadiendo el objeto i
            if peso + objetos[i][0] <= capacidad:
                mochila[i] = 1
                Cassian_Andor(i+1, peso+objetos[i][0], valor_alcanzable+objetos[i][1], mochila)
            # Soluciones sin añadir el objeto i
            if valor_alcanzable - objetos[i][1] > valor_optimo:
                mochila[i] = 0
                Cassian_Andor(i+1, peso, valor_alcanzable-objetos[i][1], mochila)
        
    n=len(objetos)
    valor_alcanzable = sum([x[1] for x in objetos])
    mochila = [0] * n
    Cassian_Andor(0, 0, valor_alcanzable, mochila)
    return (valor_optimo, mochila_opt)

precio = [103, 60, 70, 5, 15] 
n=100
pesos = [12, 23, 11, 15, 7]
objetos_a=[(12,103), (23,60), (11,70), (15,5), (7,15)]
valor_optimo = 0
mochila_opt = [0] * n 
print(mochila_Cassian_Andor(objetos_a, 100))