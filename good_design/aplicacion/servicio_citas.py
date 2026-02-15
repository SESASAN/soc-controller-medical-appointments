from dominio.cita import Cita


class ServicioCitas:
    """
    Servicio de Aplicación:
    - Orquesta el caso de uso.
    - Coordina validación, precio, persistencia y notificación.
    """

    def __init__(self, servicio_disponibilidad, servicio_precios, repositorio, servicio_notificaciones):
        self._servicio_disponibilidad = servicio_disponibilidad
        self._servicio_precios = servicio_precios
        self._repositorio = repositorio
        self._servicio_notificaciones = servicio_notificaciones

    def crear_cita(self, correo_paciente: str, id_doctor: str, fecha: str) -> None:

        if not self._servicio_disponibilidad.esta_disponible(id_doctor, fecha):
            raise Exception("El doctor no está disponible.")

        precio = self._servicio_precios.calcular_precio(id_doctor)

        cita = Cita(
            correo_paciente=correo_paciente,
            id_doctor=id_doctor,
            fecha=fecha,
            precio=precio
        )

        self._repositorio.guardar(cita)
        self._servicio_notificaciones.enviar_confirmacion(correo_paciente, cita)