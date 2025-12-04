Dashboard - API REST
====================

El Dashboard proporciona una vista general del estado de la cuenta del usuario, incluyendo el saldo actual y el resumen de transacciones recientes.

Endpoints del Dashboard
-----------------------

Obtener Información del Dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Devuelve el saldo actual del usuario y sus transacciones recientes.

**Endpoint:**

.. code-block:: http

   GET /api/dashboard

**Headers:**

.. code-block:: http

   Authorization: Bearer {token}
   Content-Type: application/json

**Respuesta Exitosa (200 OK):**

.. code-block:: json

   {
     "saldo": 5000.00,
     "transaccionesRecientes": [
       {
         "id": 1,
         "tipo": "ENVIO",
         "monto": 500.00,
         "destinatario": "usuario@example.com",
         "fecha": "2025-12-03T10:30:00",
         "estado": "COMPLETADA"
       },
       {
         "id": 2,
         "tipo": "RECEPCION",
         "monto": 1000.00,
         "remitente": "otro@example.com",
         "fecha": "2025-12-02T15:45:00",
         "estado": "COMPLETADA"
       }
     ],
     "estadisticas": {
       "totalEnviado": 2500.00,
       "totalRecibido": 7500.00,
       "numeroTransacciones": 15
     }
   }

**Códigos de Error:**

- **401 Unauthorized**: Token inválido o expirado
- **403 Forbidden**: No tiene permisos para acceder
- **500 Internal Server Error**: Error del servidor

Estructura de Datos
-------------------

Transacción
~~~~~~~~~~~

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Campo
     - Tipo
     - Descripción
   * - id
     - Long
     - Identificador único de la transacción
   * - tipo
     - String
     - Tipo de transacción (ENVIO, RECEPCION, SOLICITUD)
   * - monto
     - Double
     - Monto de la transacción
   * - destinatario
     - String
     - Email del usuario que recibe el dinero
   * - remitente
     - String
     - Email del usuario que envía el dinero
   * - fecha
     - DateTime
     - Fecha y hora de la transacción
   * - estado
     - String
     - Estado de la transacción (PENDIENTE, COMPLETADA, RECHAZADA)

Estadísticas
~~~~~~~~~~~~

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Campo
     - Tipo
     - Descripción
   * - totalEnviado
     - Double
     - Total de dinero enviado por el usuario
   * - totalRecibido
     - Double
     - Total de dinero recibido por el usuario
   * - numeroTransacciones
     - Integer
     - Cantidad total de transacciones realizadas

Ejemplo de Implementación
--------------------------

JavaScript (Frontend)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   async function obtenerDashboard() {
     const token = localStorage.getItem('token');
     
     try {
       const response = await fetch('http://localhost:8080/api/dashboard', {
         method: 'GET',
         headers: {
           'Authorization': `Bearer ${token}`,
           'Content-Type': 'application/json'
         }
       });
       
       if (response.ok) {
         const data = await response.json();
         console.log('Saldo:', data.saldo);
         console.log('Transacciones:', data.transaccionesRecientes);
         return data;
       } else {
         throw new Error('Error al obtener dashboard');
       }
     } catch (error) {
       console.error('Error:', error);
     }
   }

Java (Backend - Controller)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

   @RestController
   @RequestMapping("/api/dashboard")
   public class DashboardController {
       
       @Autowired
       private DashboardService dashboardService;
       
       @GetMapping
       public ResponseEntity<DashboardResponse> getDashboard(
           @AuthenticationPrincipal UserDetails userDetails
       ) {
           DashboardResponse dashboard = dashboardService
               .getDashboardData(userDetails.getUsername());
           return ResponseEntity.ok(dashboard);
       }
   }

Notas Importantes
-----------------

.. note::

   El Dashboard se actualiza en tiempo real cada vez que se realiza una transacción.
   Las transacciones recientes muestran las últimas 10 operaciones del usuario.

.. warning::

   El token JWT debe ser válido y no estar expirado para acceder a este endpoint.
   La sesión expira después de 24 horas de inactividad.
