Dashboard - API REST
====================

El Dashboard proporciona una vista general del estado de la cuenta del usuario, incluyendo el saldo actual y el resumen de transacciones recientes.

.. image:: _static/fastapi_1.jpg
   :alt: BillCash Digital Wallet API
   :align: center
   :width: 100%

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

🔒 = Requiere Autenticación

**transacciones**

.. image:: _static/fastapi_6.jpg
   :alt: Endpoints de transacciones
   :align: center
   :width: 100%

**solicitudes**

.. image:: _static/fastapi_7.jpg
   :alt: Endpoints de solicitudes
   :align: center
   :width: 100%

**notificaciones**

.. image:: _static/fastapi_8.jpg
   :alt: Endpoints de notificaciones
   :align: center
   :width: 100%

**categorias**

.. image:: _static/fastapi_9.jpg
   :alt: Endpoints de categorías
   :align: center
   :width: 100%

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

Schemas de Solicitudes
~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_12.jpg
   :alt: Schemas de solicitudes
   :align: center
   :width: 80%

Schemas de Notificaciones
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_13.jpg
   :alt: Schemas de notificaciones
   :align: center
   :width: 80%

Schemas de Categorías
~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_14.jpg
   :alt: Schemas de categorías
   :align: center
   :width: 80%

Ejemplo de Implementación
--------------------------

Registro de Usuario
~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_15.jpg
   :alt: Endpoint de registro
   :align: center
   :width: 100%

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

.. code-block:: bash

   curl -X GET "http://localhost:8000/usuarios/me" \
     -H "Authorization: Bearer {tu_token_jwt}"

Actualizar Usuario
~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_18.jpg
   :alt: Endpoint actualizar usuario
   :align: center
   :width: 100%

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

Crear Solicitud
~~~~~~~~~~~~~~~

.. image:: _static/fastapi_20.jpg
   :alt: Endpoint crear solicitud
   :align: center
   :width: 100%

Listar Notificaciones
~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_21.jpg
   :alt: Endpoint listar notificaciones
   :align: center
   :width: 100%

Gestión de Categorías
~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_22.jpg
   :alt: Endpoint gestión de categorías
   :align: center
   :width: 100%

JavaScript (Fetch API)
~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/fastapi_23.jpg
   :alt: Ejemplos de implementación JavaScript
   :align: center
   :width: 100%

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

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

Estas interfaces permiten probar los endpoints directamente desde el navegador.
