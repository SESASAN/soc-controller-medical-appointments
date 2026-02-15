class Cita:
    """
    Entidad del dominio.
    Representa una cita médica.
    """

    def __init__(self, correo_paciente: str, id_doctor: str, fecha: str, precio: int):
        self.correo_paciente = correo_paciente
        self.id_doctor = id_doctor
        self.fecha = fecha
        self.precio = precio

    def __repr__(self):
        return (
            f"Cita(correo={self.correo_paciente}, "
            f"doctor={self.id_doctor}, fecha={self.fecha}, precio={self.precio})"
        )