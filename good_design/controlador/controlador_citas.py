class ControladorCitas:
    """
    GRASP Controller:
    - Recibe la solicitud externa.
    - Delegar al servicio de aplicación.
    - No contiene lógica de negocio.
    """

    def __init__(self, servicio_citas):
        self._servicio_citas = servicio_citas

    def crear_cita(self, correo_paciente: str, id_doctor: str, fecha: str) -> None:
        self._servicio_citas.crear_cita(correo_paciente, id_doctor, fecha)