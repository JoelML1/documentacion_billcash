# Manual de Usuario — BillCash (Actualizado)

Este manual de usuario reúne las funcionalidades principales de la aplicación BillCash y documenta las últimas implementaciones realizadas en el proyecto (según el repositorio BillCash-Oficial/Proyecto-BillCash). El objetivo es que el equipo de producto, soporte y usuarios finales cuenten con instrucciones claras para las acciones más comunes.

---

## Índice
- Introducción
- Novedades (resumen de implementaciones técnicas relevantes)
- Olvidé mi contraseña
  - Solicitar restablecimiento
  - Correo de recuperación (plantilla)
  - Confirmación de actualización
  - Buenas prácticas de seguridad
- Solicitudes de dinero
  - Ver y gestionar solicitudes
  - Enviar una solicitud
  - Aceptar / rechazar / cancelar
  - Estados y notificaciones
- Pago de servicios
  - Pagar un servicio
  - Confirmación y recibo
  - Pagos programados y historial
- Movimientos
  - Tipos de movimiento y campos
  - Búsquedas, filtros y exportación
  - Investigar movimientos
- Tarjetas
  - Visualizar y gestionar tarjetas
  - Añadir / verificar / bloquear / eliminar
  - Seguridad y límites
- Anexos y referencias técnicas

---

## Introducción
Bienvenido a BillCash. Este manual explica las funciones principales que un usuario puede utilizar en la aplicación: recuperar contraseña, gestionar solicitudes de dinero, pagar servicios, revisar movimientos y administrar tarjetas.

## Novedades (resumen técnico)
En el repositorio principal del proyecto se han implementado o documentado las siguientes características que afectan al manual de usuario y al comportamiento de la aplicación:
- Sistema de recuperación de contraseña con correo de restablecimiento y enlace con expiración (ver GUIA_RECUPERACION_CONTRASENA.md).
- Sistema de correos automáticos y plantillas (SISTEMA_CORREOS_AUTOMATICOS.md). Las notificaciones por correo siguen plantillas con botón de acción y expiración de enlaces.
- Validación de email implementada para flujos de registro y recuperación (VALIDACION_EMAIL_IMPLEMENTADA.md).
- Sistema de solicitudes de dinero con estados y notificaciones (SISTEMA_SOLICITUDES_DINERO.md).
- Sistema de pagos de servicios (SISTEMA_PAGOS_SERVICIOS.md) con comprobantes y registro en movimientos.
- Documentación de despliegue y configuración (varios archivos en el repo: DESPLIEGUE_RAPIDO.md, RAILWAY_DEPLOYMENT.md, BREVO_SETUP_COMPLETO.md) que no afectan directamente al usuario final pero son relevantes para soporte y operaciones.

Referencia técnica: https://github.com/BillCash-Oficial/Proyecto-BillCash

---

## Olvidé mi contraseña

1) Solicitar restablecimiento
- Desde la pantalla de login el usuario pulsa "¿Olvidaste tu contraseña?".
- Se abre un modal donde ingresa su correo y pulsa "Enviar instrucciones".
- Si el correo existe en el sistema se envía un correo con enlace para restablecerla.

2) Correo de recuperación (plantilla)
- El correo incluye saludo, explicación, botón "Restablecer Contraseña", y nota sobre la expiración del enlace (1 hora por defecto).
- Ejemplo de asunto: "Recuperación de Contraseña — BillCash".
- Si no solicitaste el cambio, el usuario debe ignorar el correo.

3) Confirmación de actualización
- Una vez creada la nueva contraseña se muestra una pantalla de éxito y se redirige al login.
- Mensaje: "¡Contraseña Actualizada! Tu contraseña ha sido restablecida exitosamente."

4) Buenas prácticas y seguridad
- El enlace usa un token único con expiración corta.
- Limitar reintentos y proteger contra enumeración de cuentas.
- Requerir contraseña fuerte y mostrar feedback en tiempo real.

---

## Solicitudes de dinero

1) Ver y gestionar solicitudes
- La sección "Solicitudes de Dinero" muestra solicitudes recibidas, enviadas y el historial.
- Si no hay solicitudes pendientes aparece un mensaje claro: "No tienes solicitudes pendientes".

2) Enviar una solicitud
- Pasos: seleccionar destinatario, ingresar monto, concepto y enviar.
- El receptor recibe notificación y puede aceptar o rechazar.

3) Aceptar / rechazar / cancelar
- Aceptar: se realiza la transferencia desde saldo o tarjeta configurada.
- Rechazar: notifica al emisor.
- Cancelar: el emisor puede cancelar una solicitud pendiente (según permisos).

4) Estados y notificaciones
- Estados: Pendiente, Aceptada, Rechazada, Expirada.
- Notificaciones push/correo cuando cambie el estado.

---

## Pago de servicios

1) Pagar un servicio
- Ir a "Pago de Servicios".
- Seleccionar proveedor o ingresar referencia (número de contrato/cliente).
- Elegir método de pago (saldo, tarjeta guardada) y confirmar.

2) Confirmación y recibo
- Después del pago se muestra comprobante con referencia, comisión (si aplica) y estado.
- El comprobante se envía por correo y se registra en Movimientos.

3) Pagos programados y historial
- Posibilidad de programar pagos recurrentes.
- Historial filtrable por proveedor y fechas.

---

## Movimientos

Tipos de movimiento: Ingresos, Egresos, Transferencias, Solicitudes, Comisiones.

Campos mostrados en cada registro:
- Fecha y hora
- Tipo
- Monto
- Saldo posterior
- Referencia / ID
- Contraparte (nombre/correo)
- Estado

Búsqueda y filtros: por fecha, tipo, proveedor, referencia. Exportación a CSV/PDF.

Opciones: ver detalles, descargar comprobante, reportar problema.

---

## Tarjetas

Visualización: lista de tarjetas con últimos 4 dígitos, marca, y estado.

Acciones: Añadir (ingresar número, vencimiento, CVV), verificar (microcargo o token), establecer predeterminada, bloquear, eliminar.

Seguridad: límites diarios, 3D Secure, y registro de eventos.

---

## Anexos y referencias técnicas
- Ver en el repositorio técnico (BillCash-Oficial/Proyecto-BillCash) los documentos de referencia:
  - GUIA_RECUPERACION_CONTRASENA.md
  - SISTEMA_CORREOS_AUTOMATICOS.md
  - SISTEMA_SOLICITUDES_DINERO.md
  - SISTEMA_PAGOS_SERVICIOS.md
  - VALIDACION_EMAIL_IMPLEMENTADA.md
  - DESPLIEGUE_RAPIDO.md / RAILWAY_DEPLOYMENT.md

---

Si prefieres, puedo:
- Añadir capturas (image1..image4) al directorio docs/images/ y referenciarlas desde este manual (necesitaré permiso para subir las imágenes).
- Ajustar el tono y microcopy.
- Separar el manual en varios archivos por sección (por ejemplo docs/olvidé_contraseña.md, docs/solicitudes.md, etc.).
