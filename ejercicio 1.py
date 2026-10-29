class Cola:
    """Cola (FIFO) implementada sobre una lista."""

    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.es_vacia():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)

    def frente(self):
        if self.es_vacia():
            raise IndexError("La cola está vacía")
        return self.items[0]

    def es_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def sumar_colas(cola_a, cola_b):
    """Recibe 2 colas de enteros y devuelve una nueva cola con la suma
    uno a uno. Si una cola es más larga, los elementos sobrantes se
    suman con 0. Las colas originales quedan intactas."""
    resultado = Cola()
    aux_a = Cola()
    aux_b = Cola()

    while not cola_a.es_vacia() or not cola_b.es_vacia():
        a = 0
        b = 0
        if not cola_a.es_vacia():
            a = cola_a.desencolar()
            aux_a.encolar(a)
        if not cola_b.es_vacia():
            b = cola_b.desencolar()
            aux_b.encolar(b)
        resultado.encolar(a + b)

    # Restaurar las colas originales
    while not aux_a.es_vacia():
        cola_a.encolar(aux_a.desencolar())
    while not aux_b.es_vacia():
        cola_b.encolar(aux_b.desencolar())

    return resultado


if __name__ == "__main__":
    cola_a = Cola()
    cola_b = Cola()

    for n in [3, 4, 2, 8, 12]:
        cola_a.encolar(n)
    for n in [6, 2, 9, 11, 3]:
        cola_b.encolar(n)

    resultado = sumar_colas(cola_a, cola_b)

    print("Cola A:        ", cola_a)
    print("Cola B:        ", cola_b)
    print("Cola Resultado:", resultado)
    # Salida esperada: [9, 6, 11, 19, 15]
