class ElementoNodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijo_izq = None
        self.hijo_der = None

class ArbolOrdenado:
    def __init__(self):
        self.nodo_raiz = None

    def insertar(self, dato):
        if not self.nodo_raiz:
            self.nodo_raiz = ElementoNodo(dato)
        else:
            self._insertar(dato, self.nodo_raiz)

    def _insertar(self, dato, nodo_actual):
        if dato <= nodo_actual.dato:
            if nodo_actual.hijo_izq is None:
                nodo_actual.hijo_izq = ElementoNodo(dato)
            else:
                self._insertar(dato, nodo_actual.hijo_izq)
        else:
            if nodo_actual.hijo_der is None:
                nodo_actual.hijo_der = ElementoNodo(dato)
            else:
                self._insertar(dato, nodo_actual.hijo_der)

    def inorden(self):
        return self._inorden(self.nodo_raiz, [])

    def _inorden(self, nodo_actual, acumulador):
        if nodo_actual:
            self._inorden(nodo_actual.hijo_izq, acumulador)
            acumulador.append(nodo_actual.dato)
            self._inorden(nodo_actual.hijo_der, acumulador)
        return acumulador

    def preorden(self):
        return self._preorden(self.nodo_raiz, [])

    def _preorden(self, nodo_actual, acumulador):
        if nodo_actual:
            acumulador.append(nodo_actual.dato)
            self._preorden(nodo_actual.hijo_izq, acumulador)
            self._preorden(nodo_actual.hijo_der, acumulador)
        return acumulador

    def postorden(self):
        return self._postorden(self.nodo_raiz, [])

    def _postorden(self, nodo_actual, acumulador):
        if nodo_actual:
            self._postorden(nodo_actual.hijo_izq, acumulador)
            self._postorden(nodo_actual.hijo_der, acumulador)
            acumulador.append(nodo_actual.dato)
        return acumulador

def calcular_valles(ruta):
    nivel = 0
    cantidad_valles = 0
    dentro_valle = False

    for paso in ruta:
        if paso == 'U':
            nivel += 1
            if nivel == 0 and dentro_valle:
                cantidad_valles += 1
                dentro_valle = False
        else:  # paso == 'D'
            if nivel == 0:
                dentro_valle = True
            nivel -= 1

    return cantidad_valles

def main():
    # Ejemplo de uso para contar valles
    ruta = "DDUUDDUDUUUD"
    print("Ejemplo de contar valles:")
    print(f"La cantidad de valles en la ruta '{ruta}' es: {calcular_valles(ruta)}\n")

    # Ejemplo de uso para el Árbol Binario Ordenado
    print("Ejemplo de Árbol Binario Ordenado:")
    arbol = ArbolOrdenado()
    for dato in [5, 3, 7, 2, 4, 6, 8]:
        arbol.insertar(dato)

    print("Recorrido Inorden (izquierdo, raíz, derecho):")
    print(arbol.inorden())

    print("\nRecorrido Preorden (raíz, izquierdo, derecho):")
    print(arbol.preorden())

    print("\nRecorrido Postorden (izquierdo, derecho, raíz):")
    print(arbol.postorden())

if __name__ == "__main__":
    main()
