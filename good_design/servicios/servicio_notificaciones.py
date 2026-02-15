class ServicioNotificaciones:
    """
    Concern: Infraestructura externa (correo).
    """

    def enviar_confirmacion(self, correo: str, cita) -> None:
        print(f"[Notificaciones] Enviando confirmación a {correo} para {cita}")