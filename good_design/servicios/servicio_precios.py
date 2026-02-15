class ServicioPrecios:
    """
    Concern: Reglas de negocio relacionadas con precios.
    """

    def calcular_precio(self, id_doctor: str) -> int:
        if id_doctor.startswith("CARD"):
            return 150
        return 100