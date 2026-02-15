class SistemaCitasMedicas:
    """
    DISEÑO MALO:
    - Mezcla múltiples responsabilidades en una sola clase.
    - Viola Separation of Concerns.
    - Actúa como Fat Controller implícito.
    """

    def crear_cita(self, correo_paciente: str, id_doctor: str, fecha: str) -> None:

        # Validación (concern: disponibilidad)
        if not self._validar_disponibilidad_doctor(id_doctor, fecha):
            raise Exception("El doctor no está disponible.")

        # Lógica de negocio (concern: cálculo de precio)
        precio = self._calcular_precio(id_doctor)

        # Persistencia (concern: base de datos)
        self._guardar_cita_en_base_datos(correo_paciente, id_doctor, fecha, precio)

        # Infraestructura (concern: notificación)
        self._enviar_correo_confirmacion(correo_paciente)

    def _validar_disponibilidad_doctor(self, id_doctor: str, fecha: str) -> bool:
        print(f"Verificando disponibilidad del doctor {id_doctor} en {fecha}...")
        return True

    def _calcular_precio(self, id_doctor: str) -> int:
        if id_doctor.startswith("CARD"):
            return 150
        return 100

    def _guardar_cita_en_base_datos(self, correo: str, id_doctor: str, fecha: str, precio: int) -> None:
        print(f"Guardando cita: {correo}, {id_doctor}, {fecha}, Precio: {precio}")

    def _enviar_correo_confirmacion(self, correo: str) -> None:
        print(f"Enviando confirmación a {correo}")