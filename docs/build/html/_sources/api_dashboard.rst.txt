Dashboard - API REST
====================

El Dashboard proporciona una vista general del estado de la cuenta del usuario, incluyendo el saldo actual y el resumen de transacciones recientes.

.. image:: _static/fastapi_1.jpg
   :alt: BillCash Digital Wallet API
   :align: center
   :width: 100%

*Imagen 1: Interfaz principal de la API de BillCash mostrando la documentación interactiva generada automáticamente por FastAPI. Esta vista presenta todos los endpoints disponibles organizados por categorías.*

Vista General de la API
-----------------------

BillCash Digital Wallet API v1.0.0 (OAS 3.1) - API para wallet digital BillCash con FastAPI y MySQL.

Endpoints Disponibles
---------------------

**default**

- ``GET /`` - Root
- ``GET /health`` - Health Check

.. image:: _static/fastapi_4.jpg
   :alt: Endpoints default
   :align: center
   :width: 100%

*Imagen 4: Endpoints básicos de la API. El endpoint Root (/) devuelve información general del servicio, mientras que Health Check (/health) verifica el estado de la aplicación y la conexión a la base de datos.*

**usuarios**

- ``POST /usuarios/login-json`` - Login Json
- ``POST /usuarios/registro`` - Registrar Usuario
- ``GET /usuarios/`` - Listar Usuarios 🔒
- ``GET /usuarios/me`` - Get My Profile 🔒
- ``GET /usuarios/me/complete`` - Get My Complete Profile 🔒
- ``GET /usuarios/buscar`` - Buscar Usuarios Publicos
- ``GET /usuarios/{usuario_id}`` - Obtener Usuario
- ``PUT /usuarios/{usuario_id}`` - Actualizar Usuario 🔒
- ``DELETE /usuarios/{usuario_id}`` - Eliminar Usuario 🔒
- ``GET /usuarios/test-endpoint`` - Test Endpoint 🔒
- ``DELETE /usuarios/eliminar-mi-cuenta`` - Eliminar Mi Cuenta 🔒
- ``DELETE /usuarios/account/delete`` - Eliminar Cuenta Completa Nueva Ruta 🔒
- ``DELETE /usuarios/eliminar-cuenta-completa`` - Eliminar Cuenta Completa 🔒
- ``GET /usuarios/verificar-email/{token}`` - Verificar Email
- ``POST /usuarios/reenviar-verificacion`` - Reenviar Verificacion
- ``POST /usuarios/solicitar-recuperacion`` - Solicitar Recuperacion Contraseña
- ``POST /usuarios/restablecer-contrasena`` - Restablecer Contraseña

.. image:: _static/fastapi_5.jpg
   :alt: Endpoints de usuarios
   :align: center
   :width: 100%

*Imagen 5: Conjunto completo de endpoints para la gestión de usuarios. Incluye operaciones de autenticación (login, registro), consulta de perfiles, actualización de datos, eliminación de cuentas y recuperación de contraseñas. Los endpoints marcados con candado requieren autenticación JWT.*

🔒 = Requiere Autenticación

**transacciones**

.. image:: _static/fastapi_6.jpg
   :alt: Endpoints de transacciones
   :align: center
   :width: 100%

*Imagen 6: Endpoints para la gestión de transacciones financieras. Permite crear, consultar, listar y eliminar transacciones entre usuarios de la wallet digital. Incluye filtros por usuario, fecha y tipo de transacción.*

**solicitudes**

.. image:: _static/fastapi_7.jpg
   :alt: Endpoints de solicitudes
   :align: center
   :width: 100%

*Imagen 7: Endpoints para el manejo de solicitudes de dinero entre usuarios. Los usuarios pueden crear solicitudes de pago, aceptarlas, rechazarlas o cancelarlas. Incluye consultas por estado (pendiente, aceptada, rechazada).*

**notificaciones**

.. image:: _static/fastapi_8.jpg
   :alt: Endpoints de notificaciones
   :align: center
   :width: 100%

*Imagen 8: Sistema de notificaciones en tiempo real. Permite listar, marcar como leídas y eliminar notificaciones del usuario. Las notificaciones se generan automáticamente ante eventos como transacciones recibidas, solicitudes de dinero o cambios en el estado de la cuenta.*

**categorias**

.. image:: _static/fastapi_9.jpg
   :alt: Endpoints de categorías
   :align: center
   :width: 100%

*Imagen 9: Gestión de categorías para clasificar transacciones. Los usuarios pueden crear categorías personalizadas (Alimentación, Transporte, Entretenimiento, etc.) para organizar mejor sus gastos e ingresos.*

Autenticación
-------------

La API utiliza autenticación Bearer Token (JWT). Para acceder a los endpoints protegidos, debes incluir el token en el header:

.. code-block:: http

   Authorization: Bearer {tu_token_jwt}

Obtener Perfil de Usuario
--------------------------

Endpoint para obtener el perfil completo del usuario autenticado.

.. image:: _static/fastapi_2.jpg
   :alt: Endpoint Actualizar Usuario
   :align: center
   :width: 100%

*Imagen 2: Detalle del endpoint PUT /usuarios/{usuario_id} en Swagger UI. Muestra los parámetros requeridos, el esquema del request body y las posibles respuestas. Permite actualizar información personal del usuario como nombres, apellidos, edad, dirección y documento de identidad.*

**Endpoint:**

.. code-block:: http

   PUT /usuarios/{usuario_id}

**Parámetros de Ruta:**

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Parámetro
     - Tipo
     - Descripción
   * - usuario_id
     - integer
     - ID del usuario a actualizar (requerido)

**Request Body (application/json):**

.. code-block:: json

   {
     "nombres": "string",
     "apellidos": "string",
     "edad": 0,
     "direccion": "user@example.com",
     "numero_documento": "string",
     "tipo_documento": "string",
     "saldo_total": 0,
     "rol": "string"
   }

**Respuestas:**

- **200 Successful Response** - Usuario actualizado correctamente
- **422 Validation Error** - Error de validación en los datos

**Ejemplo de Respuesta Exitosa:**

.. image:: _static/fastapi_3.jpg
   :alt: Esquema de respuesta UserProfileComplete
   :align: center
   :width: 80%

*Imagen 3: Esquema del modelo UserProfileComplete que define la estructura de datos devuelta al consultar el perfil completo de un usuario. Incluye todos los campos con sus tipos de datos y validaciones correspondientes.*

.. code-block:: json

   {
     "id_usuario": 0,
     "nombres": "string",
     "apellidos": "string",
     "correo": "string",
     "telefono": "string",
     "numero_documento": "string",
     "tipo_documento": "string",
     "saldo_total": 0
   }

Estructura de Datos
-------------------

UserProfileComplete
~~~~~~~~~~~~~~~~~~~

Esquema completo del perfil de usuario.

.. image:: _static/fastapi_10.jpg
   :alt: Schema UserProfileComplete
   :align: center
   :width: 80%

*Imagen 10: Visualización completa del schema UserProfileComplete en Swagger. Muestra la estructura JSON con todos los campos del perfil de usuario, incluyendo tipos de datos, restricciones y valores de ejemplo para cada propiedad.*

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Campo
     - Tipo
     - Descripción
   * - id_usuario
     - integer
     - Identificador único del usuario
   * - nombres
     - string
     - Nombres del usuario
   * - apellidos
     - string
     - Apellidos del usuario
   * - correo
     - string (email)
     - Correo electrónico del usuario
   * - telefono
     - string | null
     - Número de teléfono (opcional)
   * - numero_documento
     - string
     - Número de documento de identidad
   * - tipo_documento
     - string
     - Tipo de documento (CC, TI, CE, etc.)
   * - saldo_total
     - number
     - Saldo actual en la cuenta

Schemas de Transacciones
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_11.jpg
   :alt: Schemas de transacciones
   :align: center
   :width: 80%

*Imagen 11: Modelos de datos para transacciones. Define la estructura de TransaccionCreate (para crear nuevas transacciones), TransaccionResponse (respuesta del servidor) y TransaccionFilter (para búsquedas y filtros). Incluye campos como monto, tipo de transacción, usuario origen/destino y categoría.*

Schemas de Solicitudes
~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_12.jpg
   :alt: Schemas de solicitudes
   :align: center
   :width: 80%

*Imagen 12: Estructuras de datos para el sistema de solicitudes de dinero. Incluye SolicitudCreate, SolicitudResponse y SolicitudUpdate con campos para monto solicitado, usuario solicitante/destinatario, estado (pendiente/aceptada/rechazada) y descripción opcional.*

Schemas de Notificaciones
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_13.jpg
   :alt: Schemas de notificaciones
   :align: center
   :width: 80%

*Imagen 13: Modelos para el sistema de notificaciones. Define NotificacionCreate y NotificacionResponse con campos como título, mensaje, tipo de notificación, estado de lectura y fecha de creación. Permite mantener informados a los usuarios sobre eventos importantes.*

Schemas de Categorías
~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_14.jpg
   :alt: Schemas de categorías
   :align: center
   :width: 80%

*Imagen 14: Estructura de datos para categorías de transacciones. CategoriaCreate y CategoriaResponse incluyen nombre, descripción, icono y color para personalizar la clasificación de gastos e ingresos del usuario.*

Ejemplo de Implementación
--------------------------

Registro de Usuario
~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_15.jpg
   :alt: Endpoint de registro
   :align: center
   :width: 100%

*Imagen 15: Endpoint POST /usuarios/registro en acción. Muestra la interfaz de Swagger para crear nuevos usuarios con validación de campos obligatorios (nombres, apellidos, correo, documento) y opcionales (teléfono). La contraseña se encripta automáticamente antes de guardarse en la base de datos.*

.. code-block:: bash

   curl -X POST "http://localhost:8000/usuarios/registro" \
     -H "Content-Type: application/json" \
     -d '{
       "nombres": "Juan",
       "apellidos": "Pérez",
       "correo": "juan@example.com",
       "telefono": "3001234567",
       "numero_documento": "1234567890",
       "tipo_documento": "CC",
       "contraseña": "MiPassword123!"
     }'

Login
~~~~~

.. image:: _static/fastapi_16.jpg
   :alt: Endpoint de login
   :align: center
   :width: 100%

*Imagen 16: Endpoint POST /usuarios/login-json para autenticación. Valida credenciales (correo y contraseña) y retorna un token JWT de acceso que debe incluirse en las peticiones subsecuentes a endpoints protegidos. El token tiene una expiración configurable.*

.. code-block:: bash

   curl -X POST "http://localhost:8000/usuarios/login-json" \
     -H "Content-Type: application/json" \
     -d '{
       "correo": "juan@example.com",
       "contraseña": "MiPassword123!"
     }'

Obtener Mi Perfil
~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_17.jpg
   :alt: Endpoint obtener mi perfil
   :align: center
   :width: 100%

*Imagen 17: Endpoint GET /usuarios/me que retorna la información del usuario autenticado. Requiere token JWT en el header Authorization. Devuelve datos básicos del perfil sin información sensible como la contraseña.*

.. code-block:: bash

   curl -X GET "http://localhost:8000/usuarios/me" \
     -H "Authorization: Bearer {tu_token_jwt}"

Actualizar Usuario
~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_18.jpg
   :alt: Endpoint actualizar usuario
   :align: center
   :width: 100%

*Imagen 18: Endpoint PUT /usuarios/{usuario_id} para modificar datos del perfil. Solo el usuario propietario o administradores pueden actualizar la información. Acepta actualizaciones parciales (no es necesario enviar todos los campos).*

.. code-block:: bash

   curl -X PUT "http://localhost:8000/usuarios/1" \
     -H "Authorization: Bearer {tu_token_jwt}" \
     -H "Content-Type: application/json" \
     -d '{
       "nombres": "Juan Carlos",
       "apellidos": "Pérez García",
       "telefono": "3009876543"
     }'

Crear Transacción
~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_19.jpg
   :alt: Endpoint crear transacción
   :align: center
   :width: 100%

*Imagen 19: Endpoint para realizar transferencias de dinero entre usuarios. Valida saldo suficiente, actualiza los saldos de ambos usuarios automáticamente y registra la transacción con todos sus detalles (fecha, hora, monto, tipo, categoría). Genera notificaciones para ambas partes.*

Crear Solicitud
~~~~~~~~~~~~~~~

.. image:: _static/fastapi_20.jpg
   :alt: Endpoint crear solicitud
   :align: center
   :width: 100%

*Imagen 20: Endpoint para solicitar dinero a otros usuarios. El destinatario recibirá una notificación y podrá aceptar o rechazar la solicitud. Si se acepta, se genera automáticamente una transacción. Incluye monto solicitado, descripción opcional y estado de la solicitud.*

Listar Notificaciones
~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_21.jpg
   :alt: Endpoint listar notificaciones
   :align: center
   :width: 100%

*Imagen 21: Endpoint GET para obtener todas las notificaciones del usuario autenticado. Permite filtrar por leídas/no leídas y ordenar por fecha. Incluye paginación para manejar grandes volúmenes de notificaciones eficientemente.*

Gestión de Categorías
~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_22.jpg
   :alt: Endpoint gestión de categorías
   :align: center
   :width: 100%

*Imagen 22: Endpoints CRUD completos para categorías de transacciones. Los usuarios pueden crear categorías personalizadas, modificarlas, eliminarlas y listarlas. Cada categoría puede tener nombre, descripción, icono y color para mejor visualización en dashboards y reportes.*

JavaScript (Fetch API)
~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_23.jpg
   :alt: Ejemplos de implementación JavaScript
   :align: center
   :width: 100%

*Imagen 23: Ejemplos de código JavaScript para integrar la API en aplicaciones web. Muestra cómo hacer peticiones con Fetch API, manejar autenticación con tokens, procesar respuestas JSON y gestionar errores de forma efectiva.*

.. code-block:: javascript

   // Login
   async function login(correo, contraseña) {
     const response = await fetch('http://localhost:8000/usuarios/login-json', {
       method: 'POST',
       headers: {
         'Content-Type': 'application/json'
       },
       body: JSON.stringify({ correo, contraseña })
     });
     
     const data = await response.json();
     if (response.ok) {
       localStorage.setItem('token', data.access_token);
       return data;
     }
     throw new Error(data.detail);
   }

   // Obtener perfil
   async function obtenerPerfil() {
     const token = localStorage.getItem('token');
     const response = await fetch('http://localhost:8000/usuarios/me/complete', {
       headers: {
         'Authorization': `Bearer ${token}`
       }
     });
     
     if (response.ok) {
       return await response.json();
     }
     throw new Error('Error al obtener perfil');
   }

Python (Requests)
~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_24.jpg
   :alt: Ejemplos de implementación Python
   :align: center
   :width: 100%

*Imagen 24: Ejemplos de integración en Python usando la biblioteca requests. Demuestra cómo consumir los endpoints de la API, manejar autenticación JWT, serializar/deserializar JSON y capturar excepciones para un manejo robusto de errores.*

.. code-block:: python

   import requests

   # Login
   def login(correo: str, contraseña: str):
       response = requests.post(
           'http://localhost:8000/usuarios/login-json',
           json={'correo': correo, 'contraseña': contraseña}
       )
       if response.status_code == 200:
           return response.json()
       raise Exception(response.json()['detail'])

   # Obtener perfil
   def obtener_perfil(token: str):
       headers = {'Authorization': f'Bearer {token}'}
       response = requests.get(
           'http://localhost:8000/usuarios/me/complete',
           headers=headers
       )
       if response.status_code == 200:
           return response.json()
       raise Exception('Error al obtener perfil')

Códigos de Estado HTTP
-----------------------

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Código
     - Descripción
   * - 200
     - Operación exitosa
   * - 201
     - Recurso creado exitosamente
   * - 400
     - Solicitud incorrecta
   * - 401
     - No autenticado - Token inválido o expirado
   * - 403
     - No autorizado - Sin permisos suficientes
   * - 404
     - Recurso no encontrado
   * - 422
     - Error de validación en los datos enviados
   * - 500
     - Error interno del servidor

Notas Importantes
-----------------

.. note::

   **Autenticación JWT**
   
   - El token JWT se obtiene al hacer login exitosamente
   - El token debe incluirse en el header ``Authorization: Bearer {token}``
   - Los tokens expiran después de cierto tiempo (configurable)
   - Endpoints marcados con 🔒 requieren autenticación

.. warning::

   **Seguridad**
   
   - Nunca compartas tu token JWT
   - Las contraseñas deben tener al menos 8 caracteres
   - Se recomienda usar HTTPS en producción
   - Los datos sensibles se encriptan en la base de datos

.. tip::

   **Mejores Prácticas**
   
   - Almacena el token de forma segura (localStorage, cookies seguras)
   - Implementa refresh tokens para mejorar la experiencia del usuario
   - Maneja los errores 401 para redirigir al login
   - Valida los datos en el frontend antes de enviarlos

Documentación Interactiva
--------------------------

FastAPI proporciona documentación interactiva automática:

.. image:: _static/fastapi_25.jpg
   :alt: Documentación interactiva de FastAPI
   :align: center
   :width: 100%

*Imagen 25: Interfaz completa de Swagger UI generada automáticamente por FastAPI. Permite explorar todos los endpoints, ver esquemas de datos, probar peticiones directamente desde el navegador con autenticación incluida, y descargar la especificación OpenAPI. Ideal para desarrollo, testing y comprensión rápida de la API.*

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

Estas interfaces permiten probar los endpoints directamente desde el navegador.
