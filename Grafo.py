class Arco:
    def __init__(self, vertice_inicial, vertice_final, peso:int) -> None:
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.peso = peso
    
    def __repr__(self) -> str:
        return "["+str(self.vertice_inicial)+", "+str(self.vertice_final)+"]: "+str(self.peso)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Arco):
            return False
        return self.vertice_inicial == otro.vertice_inicial and \
               self.vertice_final == otro.vertice_final and self.peso == otro.peso
    
    def __hash__(self) -> int:
        return hash(str(self))

# Clase Grafo
class GrafoListaConPesos:
    def __init__(self) -> None:
        self.__lista_vertices = dict()
    
    def __str__(self) -> str:
        return str(self.__lista_vertices)
    
    # BUSCAR VERTICE 
    def __buscarVertice(self, dato_buscar):
        return self.__lista_vertices.get(dato_buscar)
    
    # ADICIONAR VERTICE 
    def adicionarVertice(self, dato_nuevo_vertice):
        if self.__buscarVertice(dato_nuevo_vertice) is None:
            lista_adyacentes = set()
            self.__lista_vertices[dato_nuevo_vertice] = lista_adyacentes
    
    # VER VERTICE 
    def verVertices(self):
        return list(self.__lista_vertices.keys())
    
    # VER ADYACENTES 
    def verAdyacentes(self, dato_buscar):
        return list(self.__lista_vertices.get(dato_buscar))

    # ADICIONAR ARCO 
    def adicionarArco(self, vertice_inicial, vertice_final, peso:int = 0):
        busqueda_inicial = self.__buscarVertice(vertice_inicial)
        busqueda_final = self.__buscarVertice(vertice_final)        
        if busqueda_inicial is None or busqueda_final is None:
            return False
        
        arco_nuevo = Arco(vertice_inicial, vertice_final, peso)
        busqueda_inicial.add(arco_nuevo)
    
    # SI SON ADYACENTES
    def sonAdyacentes(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.__buscarVertice(vertice_inicial)
        busqueda_final = self.__buscarVertice(vertice_final)
        if busqueda_inicial is None or busqueda_final is None:
            return False
        for arco in busqueda_inicial:
            if arco.vertice_final == vertice_final:
                return True
        return False   

    # RECORRIDO EN ANCHURA (BFS)
    def __bfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        cola_ady = [vertice_actual]
        while cola_ady:
            vertice_cola = cola_ady.pop(0)        
            adyacentes_actual_cola = self.__buscarVertice(vertice_cola)
            for arco_ady_actual in adyacentes_actual_cola:
                ady_actual = arco_ady_actual.vertice_final
                if ady_actual not in set_visitados:
                    list_recorrido.append(ady_actual)
                    set_visitados.add(ady_actual)
                    cola_ady.append(ady_actual)
        return list_recorrido, set_visitados

    def recorrerAnchura(self, vertice_inicial):
        if self.__buscarVertice(vertice_inicial) is None:
            return None        
        recorrido, visitados = self.__bfs(list(), set(), vertice_inicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__bfs(recorrido, visitados, vertice)
        return recorrido

    # CAMINO MÁS CORTO 
    def caminoMasCorto(self, vertice_inicio, vertice_fin):
        distancias = {vertice: float('inf') for vertice in self.verVertices()}
        predecesores = {vertice: None for vertice in self.verVertices()}
        distancias[vertice_inicio] = 0

        for _ in range(len(self.verVertices()) - 1):
            for vertice in self.verVertices():
                for arco in self.__buscarVertice(vertice):
                    if distancias[vertice] != float('inf') and distancias[vertice] + arco.peso < distancias[arco.vertice_final]:
                        distancias[arco.vertice_final] = distancias[vertice] + arco.peso
                        predecesores[arco.vertice_final] = vertice

        camino = []
        vertice_actual = vertice_fin
        while vertice_actual is not None:
            camino.insert(0, vertice_actual)
            vertice_actual = predecesores[vertice_actual]

        return camino, distancias[vertice_fin]
    
    # RECORRIDO POR PROFUNDIDAD 
    def __dfs(self, vertice_actual, set_visitados, list_recorrido):
        set_visitados.add(vertice_actual)
        list_recorrido.append(vertice_actual)
        adyacentes_actual = self.__buscarVertice(vertice_actual)
        for arco_ady_actual in adyacentes_actual:
            ady_actual = arco_ady_actual.vertice_final
            if ady_actual not in set_visitados:
                self.__dfs(ady_actual, set_visitados, list_recorrido)
        return list_recorrido, set_visitados

    def recorrerProfundidad(self, vertice_inicial):
        if self.__buscarVertice(vertice_inicial) is None:
            return None
        recorrido, visitados = self.__dfs(vertice_inicial, set(), list())
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__dfs(vertice, visitados, recorrido)
        return recorrido
    
    # SUMAR ARCOS 
    def contarPesos(self):
        total_pesos = 0
        for vertice in self.__lista_vertices:
            for arco in self.__lista_vertices[vertice]:
                total_pesos += arco.peso
        return total_pesos

    # PROMEDIO DE PESOS 
    def pesoPromedio(self):
        total_pesos = 0
        total_arcos = 0
        for vertice in self.__lista_vertices:
            for arco in self.__lista_vertices[vertice]:
                total_pesos += arco.peso
                total_arcos += 1
        if total_arcos == 0:
            return 0
        return total_pesos / total_arcos

    # ENCONTRAR MAYOR PESO
    def arcoMayorPeso(self):
        arco_max = None
        for vertice in self.__lista_vertices:
            for arco in self.__lista_vertices[vertice]:
                if arco_max is None or arco.peso > arco_max.peso:
                    arco_max = arco
        return arco_max

    # ENCONTRAR MENOR PESO
    def arcoMenorPeso(self):
        arco_min = None
        for vertice in self.__lista_vertices:
            for arco in self.__lista_vertices[vertice]:
                if arco_min is None or arco.peso < arco_min.peso:
                    arco_min = arco
        return arco_min

    # SUMAR ENTRE 2 VERTICES 
    def sumaPesosEntreVertices(self, vertice_inicial, vertice_final):
        peso_total = 0
        adyacentes_inicial = self.__buscarVertice(vertice_inicial)
        if adyacentes_inicial is None:
            return None
        for arco in adyacentes_inicial:
            if arco.vertice_final == vertice_final:
                peso_total += arco.peso
        return peso_total

    # OBTENER PESO DE UN ARCO
    def obtenerPesoArco(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.__buscarVertice(vertice_inicial)
        if busqueda_inicial is None:
            return None
        for arco in busqueda_inicial:
            if arco.vertice_final == vertice_final:
                return arco.peso
        return None