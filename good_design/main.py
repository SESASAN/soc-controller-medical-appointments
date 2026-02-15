from controlador.controlador_citas import ControladorCitas
from aplicacion.servicio_citas import ServicioCitas
from servicios.servicio_disponibilidad import ServicioDisponibilidad
from servicios.servicio_precios import ServicioPrecios
from servicios.servicio_notificaciones import ServicioNotificaciones
from infraestructura.repositorio_citas import RepositorioCitas


def main():
    servicio_disponibilidad = ServicioDisponibilidad()
    servicio_precios = ServicioPrecios()
    repositorio = RepositorioCitas()
    servicio_notificaciones = ServicioNotificaciones()

    servicio_citas = ServicioCitas(
        servicio_disponibilidad,
        servicio_precios,
        repositorio,
        servicio_notificaciones
    )

    controlador = ControladorCitas(servicio_citas)

    print("=== CREANDO CITA (DISEÑO BUENO) ===")
    controlador.crear_cita(
        correo_paciente="paciente@correo.com",
        id_doctor="CARD-101",
        fecha="2026-02-20 10:00"
    )
    print("=== FIN ===")


if __name__ == "__main__":
    main()