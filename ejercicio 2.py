import re


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


# Servicios disponibles de la compañía de seguros
SERVICIOS = {
    1: "Siniestros",
    2: "Contratación de pólizas",
    3: "Pagos y facturación",
    4: "Reclamos y consultas",
}


class SistemaAtencion:
    def __init__(self, servicios):
        self.servicios = servicios
        # Una cola por servicio (guarda los números de atención en espera)
        self.colas = {num: Cola() for num in servicios}
        # Último número entregado en cada servicio
        self.ultimo_numero = {num: 0 for num in servicios}

    def llegar_cliente(self, servicio):
        """Entrega un número de atención y lo encola en el servicio."""
        if servicio not in self.colas:
            print(f"El servicio {servicio} no existe.")
            return
        self.ultimo_numero[servicio] += 1
        numero = self.ultimo_numero[servicio]
        self.colas[servicio].encolar(numero)
        print(f"Su número de atención es: {servicio}-{numero:03d} "
              f"({self.servicios[servicio]}). "
              f"Clientes esperando: {self.colas[servicio].tamanio()}")

    def atender_cliente(self, servicio):
        """Llama al siguiente cliente de la cola del servicio elegido."""
        if servicio not in self.colas:
            print(f"El servicio {servicio} no existe.")
            return
        cola = self.colas[servicio]
        if cola.es_vacia():
            print(f"No hay clientes esperando en {self.servicios[servicio]}.")
            return
        numero = cola.desencolar()
        print(f"Llamando al número {servicio}-{numero:03d} "
              f"({self.servicios[servicio]}).")

    def mostrar_estado(self):
        print("\nEstado de las colas:")
        for num, nombre in self.servicios.items():
            print(f"  Servicio {num} - {nombre}: "
                  f"{self.colas[num].tamanio()} en espera")
        print()


def main():
    sistema = SistemaAtencion(SERVICIOS)

    print("=== Compañía de Seguros - Sistema de turnos ===")
    print("Servicios:")
    for num, nombre in SERVICIOS.items():
        print(f"  {num} - {nombre}")
    print("\nComandos:")
    print("  C<n>  -> llega un cliente al servicio n   (ej: C1)")
    print("  A<n>  -> atender al siguiente del servicio n (ej: A1)")
    print("  E     -> ver estado de las colas")
    print("  S     -> salir\n")

    while True:
        entrada = input("> ").strip().upper()

        if entrada == "S":
            print("Fin del programa.")
            break
        if entrada == "E":
            sistema.mostrar_estado()
            continue

        coincidencia = re.fullmatch(r"([CA])\s*(\d+)", entrada)
        if not coincidencia:
            print("Comando inválido. Use C<n>, A<n>, E o S.")
            continue

        accion = coincidencia.group(1)
        servicio = int(coincidencia.group(2))

        if accion == "C":
            sistema.llegar_cliente(servicio)
        else:
            sistema.atender_cliente(servicio)


if __name__ == "__main__":
    main()
