# Medical Appointments – SoC + Controller (GRASP)

Proyecto académico para demostrar la aplicación práctica de:

Separation of Concerns (SoC)

Controller (GRASP)

Se presenta una comparación entre:

- 🔴 Diseño inicial con violaciones de principios

- 🟢 Diseño refactorizado aplicando correctamente los principios

### Dominio Elegido

Sistema de Gestión de Citas Médicas

El sistema permite:

- Crear una cita médica

- Validar disponibilidad del doctor

- Calcular el precio según especialidad

- Guardar la cita en base de datos

- Enviar confirmación al paciente

Este dominio fue elegido porque permite separar claramente múltiples concerns que evolucionan de manera independiente.

---

# Versión 1 – Diseño Inicial (Violando SoC + Controller)

Ubicación:

```bad_design/```

Problema de Diseño

Se centralizó toda la lógica en una única clase:

```MedicalAppointmentSystem```

Esta clase mezcla:

| Concern           | Responsabilidad            |
| ----------------- | -------------------------- |
| Coordinación      | Orquestar creación de cita |
| Validación        | Disponibilidad del doctor  |
| Lógica de negocio | Cálculo de precio          |
| Persistencia      | Guardar en base de datos   |
| Infraestructura   | Envío de correo            |

- ❌ Violación de Separation of Concerns

- ❌ Fat Controller implícito

- ❌ Alta rigidez ante cambios

- ❌ Dificultad de testing

- ❌ Acoplamiento fuerte entre reglas y tecnología

## Razones de Cambio Mezcladas

Cada parte puede cambiar por razones distintas:

- Reglas de precio → decisiones comerciales

- Base de datos → decisión tecnológica

- Sistema de notificaciones → proveedor externo

- Validación → integración con sistema hospitalario

Sin embargo, todos los cambios afectan la misma clase.

Esto genera un diseño rígido y frágil.

---

# Versión 2 – Diseño Refactorizado (Aplicando SoC + Controller)

Ubicación:

```good_design/```

Cambios Realizados

Se aplicaron los siguientes criterios:

## Controller (GRASP)

Se introduce:

```AppointmentController```

Responsabilidad:

- Recibir la solicitud

- Delegar al servicio correspondiente

- No contiene lógica de negocio

## Separation of Concerns

El sistema se divide en capas conceptuales:

```
controlador/
aplicacion/
dominio/
servicios/
infraestructura/
```

Cada carpeta representa un concern distinto.

## Nueva Distribución de Responsabilidades
| Componente            | Responsabilidad             |
| --------------------- | --------------------------- |
| AppointmentController | Coordinar solicitud externa |
| AppointmentService    | Orquestar caso de uso       |
| AvailabilityService   | Validación                  |
| PricingService        | Reglas de negocio           |
| AppointmentRepository | Persistencia                |
| NotificationService   | Infraestructura externa     |
| Appointment (Entidad) | Modelo del dominio          |


## Beneficios del Nuevo Diseño

- ✔ Mayor mantenibilidad

- ✔ Bajo acoplamiento

- ✔ Separación clara de responsabilidades

- ✔ Mejor testabilidad (posibilidad de mocks)

- ✔ Evolución independiente por concern

| Aspecto                         | Antes | Después |
| ------------------------------- | ----- | ------- |
| Controller claro                | X    | ✔       |
| Separación de responsabilidades | X     | ✔       |
| Facilidad de testing            | Baja  | Alta    |
| Impacto de cambios              | Alto  | Bajo    |
| Estructura modular              | No    | Sí      |


El diseño refactorizado introduce:

- Más clases
- Mayor nivel de abstracción
- Más complejidad estructural inicial
- En sistemas pequeños podría parecer “sobre-diseñado”.

Sin embargo, en sistemas reales con evolución constante, esta separación reduce significativamente el costo de cambio.

---

# Cómo Ejecutar el Proyecto
## Requisitos

* Python 3.8 o superior

Para verificar tu versión de Python:

```python --version```
o
```python3 --version```

### Ejecutar la Versión con Diseño Malo

- 1️⃣ Desde la raíz del proyecto, navega a la carpeta:

```cd bad_design```

- 2️⃣ Ejecuta el archivo principal:

```python main.py```
o
```python3 main.py```

#### Salida esperada:

```
=== CREANDO CITA (DISEÑO MALO) ===
[BD] Verificando disponibilidad del doctor...
[BD] Guardando cita...
[EMAIL] Enviando confirmación...
=== FIN ===
```

En esta versión toda la lógica se ejecuta desde una sola clase, evidenciando la violación de SoC y un Fat Controller implícito.

### Ejecutar la Versión con Diseño Refactorizado

1️⃣ Desde la raíz del proyecto, navega a la carpeta:

```cd diseno_bueno```

2️⃣ Ejecuta el archivo principal:

```python main.py```
o
```python3 main.py```

#### Salida esperada:

```
=== CREANDO CITA (DISEÑO BUENO) ===
[Disponibilidad] Verificando doctor...
[Repositorio] Guardando en base de datos...
[Notificaciones] Enviando confirmación...
=== FIN ===
```

---
# Conclusión

Este proyecto demuestra que:

- SoC no es solo dividir archivos, sino separar razones de cambio.
- Controller no es una clase que haga todo, sino un coordinador del sistema.
- La correcta organización estructural mejora la mantenibilidad y claridad arquitectónica.
- El rediseño no solo mejora el código, sino que hace explícita la arquitectura conceptual del sistema.