class RepositorioCitas:
    """
    Concern: Persistencia.
    Encapsula acceso a base de datos.
    """

    def guardar(self, cita) -> None:
        print(f"[Repositorio] Guardando en base de datos: {cita}")