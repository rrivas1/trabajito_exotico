from Grafo import GrafoListaConPesos

# Crear el grafo
grafo1 = GrafoListaConPesos()

# Adicionar vértices
grafo1.adicionarVertice("Barranquilla")
grafo1.adicionarVertice("Bogota")
grafo1.adicionarVertice("Medellin")

# Adicionar arcos
grafo1.adicionarArco("Barranquilla", "Bogota", 20)
grafo1.adicionarArco("Barranquilla", "Medellin", 240)
grafo1.adicionarArco("Bogota", "Medellin", 80)

# Imprimir el grafo
print("El grafo es:\n", grafo1, sep="")

# Imprimir el recorrido BFS desde 'Barranquilla'
print("Recorrido en anchura (BFS) desde Barranquilla:", grafo1.recorrerAnchura("Barranquilla"))

# Calcular e imprimir el camino más corto desde 'Barranquilla' hasta 'Bogota'
camino, distancia = grafo1.caminoMasCorto("Barranquilla", "Bogota")
print("\nEl camino más corto de Barranquilla a Bogota es:", camino)
print("La distancia más corta es:", distancia)

# Calcular e imprimir el camino más corto desde 'Barranquilla' hasta 'Medellin'
camino, distancia = grafo1.caminoMasCorto("Barranquilla", "Medellin")
print("\nEl camino más corto de Barranquilla a Medellin es:", camino)
print("La distancia más corta es:", distancia)

# Imprimir el recorrido DFS desde 'Barranquilla'
print("\nRecorrido en profundidad (DFS) desde Barranquilla:", grafo1.recorrerProfundidad("Barranquilla"))

# Contar la suma de los pesos
suma_pesos = grafo1.contarPesos()
print("La suma de los pesos es:", suma_pesos)

# Imprimir el peso promedio
print("Peso promedio de los arcos en el grafo:", grafo1.pesoPromedio())

# Imprimir el arco con mayor peso
arco_mayor = grafo1.arcoMayorPeso()
print("Arco con mayor peso:", arco_mayor)

# Imprimir el arco con menor peso
arco_menor = grafo1.arcoMenorPeso()
print("Arco con menor peso:", arco_menor)

# Imprimir la suma de los pesos entre dos vértices
suma_pesos = grafo1.sumaPesosEntreVertices("Barranquilla", "Medellin")
print("Suma de los pesos entre los vértices Barranquilla y Medellin:", suma_pesos)

#Imprimir la obtencion del peso del arco 
peso = grafo1.obtenerPesoArco("Barranquilla", "Bogota")
print("\nPeso del arco entre Barranquilla y Bogota:", peso)

