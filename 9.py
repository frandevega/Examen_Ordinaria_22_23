# Clase para representar un vértice del grafo
class Vertice:
  def __init__(self, nombre):
    self.nombre = nombre
    self.vecinos = {}
  
  def agregarVecino(self, vecino, peso=0):
    self.vecinos[vecino] = peso
  
  def __str__(self):
    return f"{self.nombre}"

# Clase para representar un grafo
class Grafo:
  def __init__(self):
    self.vertices = {}
  
  def agregarVertice(self, vertice):
    self.vertices[vertice.nombre] = vertice
  
  def agregarArista(self, desde, hasta, peso=0):
    if desde not in self.vertices:
      self.agregarVertice(Vertice(desde))
    if hasta not in self.vertices:
      self.agregarVertice(Vertice(hasta))
    self.vertices[desde].agregarVecino(self.vertices[hasta], peso)
    self.vertices[hasta].agregarVecino(self.vertices[desde], peso)
  
  def obtenerVertice(self, nombre):
    if nombre in self.vertices:
      return self.vertices[nombre]
    return None
  
  # Método para encontrar el árbol de expansión mínima utilizando el algoritmo de Kruskal
  def arbolExpansionMinimaKruskal(self):
    arbol = Grafo()
    aristas = []
    for vertice in self.vertices.values():
      for vecino, peso in vertice.vecinos.items():
        aristas.append((peso, vertice, vecino))
    aristas = sorted(aristas)
    conjuntos = {vertice: vertice.nombre for vertice in self.vertices.values()}
    for peso, vertice, vecino in aristas:
      if conjuntos[vertice] != conjuntos[vecino]:
          arbol.agregarArista(vertice.nombre, vecino.nombre, peso)
      for vertice in conjuntos:
        if conjuntos[vertice] == conjuntos[vecino]:
            conjuntos[vertice] = conjuntos[vertice]
        return arbol
  def __str__(self):
    s = ""
    for vertice in self.vertices.values():
        s += f"{vertice.nombre} -> {vertice.vecinos.keys()} -> {vertice.vecinos.values()}n"
    return s
  def generarGrafo(self, n, m):
    for i in range(n):
      self.agregarVertice(Vertice(i))
    for i in range(m):
      desde = random.randint(0, n-1)
      hasta = random.randint(0, n-1)
      peso = random.randint(1, 100)
      self.agregarArista(desde, hasta, peso)
                
                
          
       
