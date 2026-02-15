class ServicioDisponibilidad:
    """
    Concern: Validación de disponibilidad.
    """

    def esta_disponible(self, id_doctor: str, fecha: str) -> bool:
        print(f"[Disponibilidad] Verificando doctor {id_doctor} en {fecha}")
        return True