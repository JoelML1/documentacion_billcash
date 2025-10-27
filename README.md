# BillCash - Documentación del Sistema

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-en%20desarrollo-yellow.svg)
![Documentation](https://img.shields.io/badge/docs-online-green.svg)

Documentación completa del sistema **BillCash**, una plataforma integral de gestión de pagos y facturación.

## 🌐 Ver Documentación Online

La documentación está disponible en línea en:

**📖 https://joelml1.github.io/documentacion_billcash/**

Se actualiza automáticamente cada vez que se hace push al repositorio.

## 📋 Descripción

BillCash es un sistema diseñado para facilitar el control financiero, procesamiento de transacciones y generación de reportes para empresas de todos los tamaños.

## 🚀 Características Principales

- ✅ Gestión completa de facturas y pagos
- ✅ Procesamiento de transacciones en tiempo real
- ✅ Generación de reportes financieros
- ✅ Administración de clientes y proveedores
- ✅ Integración con múltiples métodos de pago
- ✅ Automatización de procesos de cobro

## 📖 Contenido de la Documentación

### 🔧 Requisitos Funcionales
- Gestión de Usuarios
- Gestión de Facturas
- Gestión de Pagos
- Gestión de Clientes
- Reportes y Análisis
- Notificaciones
- Seguridad y Auditoría
- Configuración del Sistema

### 📱 Manual de Usuario
- Introducción y requisitos
- Registro de usuario
- Inicio de sesión
- Dashboard principal
- Enviar dinero
- Solicitar dinero
- Cartera de transacciones

### 🎯 Casos de Uso
- Diagramas detallados
- Especificaciones técnicas
- Matriz de trazabilidad
- Actores del sistema

## 📖 Documentación

La documentación está construida con [Sphinx](https://www.sphinx-doc.org/) y está disponible en formato HTML.

### Ver la Documentación

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Genera la documentación HTML:
   ```bash
   sphinx-build -b html docs/source docs/build/html
   ```

3. Abre el archivo generado:
   ```bash
   start docs/build/html/index.html  # Windows
   open docs/build/html/index.html   # macOS
   xdg-open docs/build/html/index.html  # Linux
   ```

### Estructura del Proyecto

```
.
├── docs/
│   ├── source/
│   │   ├── conf.py          # Configuración de Sphinx
│   │   ├── index.rst        # Página principal
│   │   ├── _static/         # Archivos estáticos
│   │   └── _templates/      # Plantillas personalizadas
│   ├── build/               # Documentación generada (ignorado en git)
│   ├── Makefile             # Make para Unix/macOS
│   └── make.bat             # Make para Windows
├── main.py                  # Archivo principal (placeholder)
├── requirements.txt         # Dependencias del proyecto
├── .gitignore              # Archivos ignorados por git
└── README.md               # Este archivo
```

## 📚 Contenido de la Documentación

La documentación incluye:

1. **Requisitos Funcionales** (RF-001 a RF-021)
   - Gestión de Usuarios
   - Gestión de Facturas
   - Gestión de Pagos
   - Gestión de Clientes
   - Reportes y Análisis
   - Notificaciones
   - Seguridad y Auditoría
   - Configuración del Sistema

2. **Requisitos No Funcionales**
   - Rendimiento
   - Seguridad
   - Disponibilidad
   - Escalabilidad

3. **Stack Tecnológico Recomendado**
   - Backend (Python, FastAPI/Django)
   - Frontend (React/Vue.js)
   - DevOps (Docker, Kubernetes)

## 🛠️ Tecnologías Utilizadas

- **Python 3.13+**
- **Sphinx 8.2.3** - Generador de documentación
- **reStructuredText** - Formato de marcado

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JoelML1/documentacion_billcash.git
   cd documentacion_billcash
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Unix/macOS
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Editar la Documentación

1. Edita los archivos `.rst` en `docs/source/`
2. Regenera la documentación:
   ```bash
   sphinx-build -b html docs/source docs/build/html
   ```
3. Visualiza los cambios abriendo `docs/build/html/index.html`

## 👥 Autor

- **Joel Medina** - Desarrollador Principal

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## 📞 Contacto

Para más información sobre BillCash:

- **Email:** soporte@billcash.com
- **GitHub:** [@JoelML1](https://github.com/JoelML1)
- **Repositorio:** [documentacion_billcash](https://github.com/JoelML1/documentacion_billcash)

---

⭐ Si encuentras útil este proyecto, considera darle una estrella en GitHub!
