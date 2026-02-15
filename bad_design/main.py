from sistema_citas_medicas import SistemaCitasMedicas


def main():
    sistema = SistemaCitasMedicas()

    print("=== CREANDO CITA (DISEÑO MALO) ===")
    sistema.crear_cita(
        correo_paciente="paciente@correo.com",
        id_doctor="CARD-101",
        fecha="2026-02-20 10:00"
    )
    print("=== FIN ===")


if __name__ == "__main__":
    main()