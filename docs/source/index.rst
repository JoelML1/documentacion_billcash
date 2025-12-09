.. BillCash - Documentación del Sistema

========================================
BillCash - Documentación del Sistema
========================================

.. raw:: html

   <div style="margin-bottom: 20px;">
      <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version 1.0.0" style="margin-right: 10px;">
      <img src="https://img.shields.io/badge/status-en%20desarrollo-yellow.svg" alt="En Desarrollo">
      <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python 3.9+">
      <img src="https://img.shields.io/badge/FastAPI-0.100+-green.svg" alt="FastAPI">
   </div>

Bienvenido a la Documentación de BillCash
==========================================

**BillCash** es una billetera digital moderna que permite realizar transacciones de dinero de forma segura, 
rápida y eficiente. Desarrollada con FastAPI y tecnologías modernas, BillCash ofrece una experiencia 
completa para la gestión de pagos digitales entre usuarios.

.. note::
   Esta documentación cubre la versión 1.0.0 del sistema BillCash

¿Qué es BillCash?
=================

BillCash es una plataforma de billetera digital que permite:

💰 **Gestión de Dinero**
   * Enviar y recibir dinero entre usuarios
   * Solicitar dinero a otros usuarios
   * Gestión de saldo en tiempo real
   * Historial completo de transacciones

💳 **Gestión de Tarjetas**
   * Vinculación de tarjetas de débito/crédito
   * Múltiples tarjetas por cuenta
   * Tarjetas predeterminadas para pagos rápidos

🏦 **Cuentas Bancarias**
   * Conexión con cuentas bancarias
   * Transferencias directas
   * Retiros y depósitos

🔒 **Seguridad**
   * Autenticación JWT
   * Encriptación de datos sensibles
   * Verificación de identidad
   * Auditoría de transacciones

📊 **Reportes y Análisis**
   * Dashboard con estadísticas
   * Histórico de movimientos
   * Exportación de datos

Arquitectura del Sistema
=========================

BillCash está construido con una arquitectura moderna:

* **Backend:** FastAPI (Python) - API REST
* **Base de Datos:** PostgreSQL/MySQL
* **Autenticación:** JWT (JSON Web Tokens)
* **Frontend:** React/Vue.js (aplicación web y móvil)
* **Hosting:** Cloud (Azure/AWS)

Índice de Documentación
========================

.. toctree::
   :maxdepth: 2
   :caption: 📱 Manual de Usuario

   manual_index

.. toctree::
   :maxdepth: 2
   :caption: 🔧 API REST - Documentación Técnica

   api_dashboard

.. toctree::
   :maxdepth: 2
   :caption: 📋 Casos de Uso

   casos_uso

Características Principales
============================

1. 💰 Transacciones de Dinero
------------------------------

**Enviar Dinero**
~~~~~~~~~~~~~~~~~
Los usuarios pueden enviar dinero a otros usuarios de BillCash de forma instantánea:

* Búsqueda de destinatarios por nombre de usuario o correo
* Selección de monto a enviar
* Agregar nota o concepto de pago
* Confirmación con verificación de seguridad
* Notificación en tiempo real al destinatario

**Solicitar Dinero**
~~~~~~~~~~~~~~~~~~~~
Funcionalidad para solicitar pagos a otros usuarios:

* Crear solicitud con monto específico
* Agregar descripción del motivo
* Enviar solicitud a uno o varios usuarios
* Seguimiento de solicitudes enviadas y recibidas
* Aceptar o rechazar solicitudes recibidas

**Historial de Transacciones**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Vista completa de todas las transacciones
* Filtros por tipo (enviadas, recibidas, solicitudes)
* Filtros por fecha y monto
* Exportación de historial
* Detalles completos de cada transacción

2. 💳 Gestión de Tarjetas
--------------------------

**Vinculación de Tarjetas**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Agregar tarjetas de débito y crédito
* Validación de datos de tarjeta
* Encriptación de información sensible
* Soporte para múltiples emisores

**Administración de Tarjetas**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Ver todas las tarjetas vinculadas
* Establecer tarjeta predeterminada
* Eliminar tarjetas
* Actualizar información de vencimiento

3. 🏦 Cuentas Bancarias
------------------------

**Gestión de Cuentas**
~~~~~~~~~~~~~~~~~~~~~~
* Vincular cuentas bancarias
* Ver saldo disponible
* Historial de movimientos
* Transferencias entre cuentas
* Retiros y depósitos

**Seguridad Bancaria**
~~~~~~~~~~~~~~~~~~~~~~
* Verificación de titular
* Validación de CLABE/número de cuenta
* Límites de transacción configurables
* Alertas de movimientos

4. 👤 Gestión de Usuarios
--------------------------

**Registro y Autenticación**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
El sistema implementa un proceso seguro de registro:

* Registro con nombre, email y contraseña
* Validación de correo electrónico
* Autenticación JWT
* Recuperación de contraseña
* Cierre de sesión seguro

**Perfil de Usuario**
~~~~~~~~~~~~~~~~~~~~~
Cada usuario puede gestionar su información:

* Editar datos personales
* Cambiar contraseña
* Configurar foto de perfil
* Preferencias de notificaciones
* Configuración de privacidad

5. 🔔 Notificaciones
--------------------

**Notificaciones en Tiempo Real**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Dinero recibido
* Solicitudes de dinero
* Confirmaciones de pago
* Alertas de seguridad
* Actualizaciones del sistema

**Configuración de Notificaciones**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Activar/desactivar por tipo
* Notificaciones push (móvil)
* Notificaciones email
* Notificaciones en app

6. 🔒 Seguridad y Privacidad
-----------------------------

**Seguridad del Sistema**
~~~~~~~~~~~~~~~~~~~~~~~~~
BillCash implementa múltiples capas de seguridad:

* Encriptación end-to-end
* Tokens JWT con expiración
* Hashing de contraseñas (bcrypt)
* Validación de sesiones
* Protección contra CSRF
* Rate limiting en endpoints
* Logs de auditoría

**Protección de Datos**
~~~~~~~~~~~~~~~~~~~~~~~
* Cumplimiento con GDPR
* Datos sensibles encriptados
* Solicitud de eliminación de cuenta
* Exportación de datos personales
* Políticas de privacidad claras

7. 📊 Dashboard y Estadísticas
-------------------------------

**Panel de Control**
~~~~~~~~~~~~~~~~~~~~
Vista general del estado de la cuenta:

* Saldo disponible
* Transacciones recientes
* Solicitudes pendientes
* Gráficos de gastos/ingresos
* Resumen mensual

**Reportes**
~~~~~~~~~~~~
* Reportes de movimientos
* Análisis de gastos por categoría
* Comparativas mensuales
* Exportación a PDF/Excel

Tecnologías Utilizadas
=======================

Backend - FastAPI
-----------------

**Framework Principal**
~~~~~~~~~~~~~~~~~~~~~~~
BillCash utiliza FastAPI como framework principal para la API REST:

.. code-block:: python

   from fastapi import FastAPI, HTTPException, Depends
   from fastapi.security import HTTPBearer
   
   app = FastAPI(
       title="BillCash API",
       description="API REST para billetera digital",
       version="1.0.0"
   )
   
   security = HTTPBearer()
   
   @app.get("/api/usuarios/me")
   async def obtener_usuario_actual(token: str = Depends(security)):
       """Obtiene información del usuario autenticado"""
       return {"usuario": "info"}

**Características de FastAPI**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Validación automática con Pydantic
* Documentación interactiva (Swagger/OpenAPI)
* Async/await para alto rendimiento
* Type hints de Python
* Inyección de dependencias
* Manejo robusto de errores

Base de Datos
-------------

**PostgreSQL/MySQL**
~~~~~~~~~~~~~~~~~~~~
* Almacenamiento relacional
* Transacciones ACID
* Índices optimizados
* Backup automático
* Replicación

Autenticación JWT
-----------------

**JSON Web Tokens**
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from jose import JWTError, jwt
   from datetime import datetime, timedelta
   
   def crear_token(usuario_id: int) -> str:
       payload = {
           "sub": str(usuario_id),
           "exp": datetime.utcnow() + timedelta(hours=24)
       }
       return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

Guía de Inicio Rápido
======================

Para Usuarios
-------------

1. **Registro**
   
   * Accede a la app BillCash
   * Haz clic en "Crear Cuenta"
   * Completa tus datos
   * Verifica tu correo electrónico

2. **Primera Transacción**
   
   * Vincula una tarjeta o cuenta bancaria
   * Agrega fondos a tu billetera
   * Busca un contacto
   * Envía tu primer pago

3. **Explora Funcionalidades**
   
   * Consulta :doc:`manual_index` para tutoriales detallados
   * Revisa :doc:`casos_uso` para ejemplos prácticos

Para Desarrolladores
--------------------

1. **Instalación**

.. code-block:: bash

   # Clonar repositorio
   git clone https://github.com/JoelML1/billcash.git
   cd billcash
   
   # Crear entorno virtual
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   
   # Instalar dependencias
   pip install -r requirements.txt

2. **Configuración**

.. code-block:: bash

   # Crear archivo .env
   cp .env.example .env
   
   # Configurar variables
   DATABASE_URL=postgresql://user:pass@localhost/billcash
   SECRET_KEY=tu-clave-secreta-muy-segura
   JWT_EXPIRATION=24

3. **Ejecutar**

.. code-block:: bash

   # Iniciar servidor de desarrollo
   uvicorn main:app --reload
   
   # API disponible en http://localhost:8000
   # Documentación en http://localhost:8000/docs

4. **Explorar API**
   
   * Revisa :doc:`api_dashboard` para documentación completa
   * Prueba endpoints en Swagger UI
   * Consulta ejemplos de código

Soporte y Contacto
==================

**Documentación**
   📖 Esta documentación completa

**Repositorio**
   💻 https://github.com/JoelML1/documentacion_billcash

**Issues**
   🐛 Reporta problemas en GitHub Issues

**Licencia**
   📄 MIT License

----

Índices y Búsqueda
==================

* :ref:`genindex`
* :ref:`search`

----

.. note::
   **Versión:** 1.0.0 | **Última actualización:** Diciembre 2025
   
   Para más información, visita la :doc:`api_dashboard` o consulta el :doc:`manual_index`.

Seguridad
---------

* Encriptación de datos sensibles (SSL/TLS)
* Cumplimiento con GDPR y normativas de privacidad
* Autenticación de dos factores (opcional)
* Políticas de contraseñas robustas

Disponibilidad
--------------

* Disponibilidad del 99.5% (downtime máximo de 3.65 días/año)
* Tiempo de respuesta ante incidentes: 4 horas
* Mantenimiento programado en horarios de baja actividad

Escalabilidad
-------------

* Arquitectura modular y microservicios
* Base de datos escalable horizontalmente
* Cacheo de consultas frecuentes

Tecnologías Recomendadas
=========================

Backend
-------

* **Lenguaje:** Python 3.13+
* **Framework:** FastAPI o Django
* **Base de datos:** PostgreSQL
* **Cache:** Redis
* **Mensajería:** RabbitMQ o Celery

Frontend
--------

* **Framework:** React o Vue.js
* **UI Library:** Material-UI o Ant Design
* **Gestión de estado:** Redux o Pinia

DevOps
------

* **Contenedores:** Docker
* **Orquestación:** Kubernetes
* **CI/CD:** GitHub Actions o GitLab CI
* **Monitoreo:** Prometheus + Grafana

Glosario
========

.. glossary::

   CFDI
      Comprobante Fiscal Digital por Internet (México)

   IVA
      Impuesto al Valor Agregado

   RFC
      Registro Federal de Contribuyentes (México)

   NIT
      Número de Identificación Tributaria

   PCI-DSS
      Payment Card Industry Data Security Standard

   JWT
      JSON Web Token

   API
      Application Programming Interface

Contacto y Soporte
==================

Para más información sobre BillCash:

* **Email:** soporte@billcash.com
* **Teléfono:** +57 318-428-6954
* **Sitio web:** https://www.billcash.com
* **Documentación:** https://docs.billcash.com

Índice de Contenidos
====================

.. toctree::
   :maxdepth: 2
   :caption: Documentación:

   casos_uso
   manual_index

