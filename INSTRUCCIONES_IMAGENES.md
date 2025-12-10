# 📸 Instrucciones para Guardar las Imágenes del Manual de Usuario

## Ubicación
Guarda todas las imágenes en la carpeta:
```
docs/source/_static/
```

## Nombres de las Imágenes

Según las capturas de pantalla proporcionadas, guarda cada imagen con el siguiente nombre:

### 1. Solicitudes de Dinero
**Archivo:** `solicitudes_vacio.png`
- **Descripción:** Pantalla que muestra "No tienes solicitudes pendientes"
- **Contenido:** Icono de dinero 💰, mensaje vacío, botón "Volver"

### 2. Recuperación de Contraseña - Email
**Archivo:** `recuperar_contrasena_email.png`
- **Descripción:** Email de recuperación de contraseña
- **Contenido:** "Hola Juan Diego, Recibimos una solicitud para restablecer la contraseña..."
- **Incluye:** Botón "Restablecer Contraseña", advertencia de expiración en 1 hora

### 3. Pago de Servicios
**Archivo:** `pago_servicios.png`
- **Descripción:** Pantalla principal de pago de servicios
- **Contenido:** Iconos de servicios (Luz, Agua, Gas, Internet, Televisión, Teléfono, Celular, Impuestos)
- **Incluye:** Saldo disponible en la parte superior

### 4. Restablecer Contraseña - Formulario
**Archivo:** `restablecer_contrasena.png`
- **Descripción:** Formulario para crear nueva contraseña
- **Contenido:** Logo BillCash, campos "Nueva Contraseña" y "Confirmar Contraseña"
- **Incluye:** Botones "Restablecer Contraseña" y "Volver al Login"

### 5. Contraseña Actualizada
**Archivo:** `contrasena_actualizada.png`
- **Descripción:** Confirmación de contraseña restablecida
- **Contenido:** Icono de check verde ✅, mensaje "¡Contraseña Actualizada!"
- **Incluye:** Contador de redirección, botón "Ir al Login Ahora"

### 6. Movimientos/Transacciones
**Archivo:** `movimientos.png`
- **Descripción:** Historial completo de transacciones
- **Contenido:** Tabla con columnas Fecha, Tipo, Monto (COP), Descripción
- **Incluye:** Transacciones en rojo (envíos) y verde (recepciones)

### 7. Mis Tarjetas
**Archivo:** `mis_tarjetas.png`
- **Descripción:** Gestión de tarjetas vinculadas
- **Contenido:** 3 tarjetas mostradas (CRÉDITO, DÉBITO, DÉBITO)
- **Incluye:** Botones "Bloquear" y "Eliminar", botón "+ Solicitar Nueva Tarjeta"

## Checklist de Imágenes

Marca cuando hayas guardado cada imagen:

- [ ] `solicitudes_vacio.png` - Imagen 1
- [ ] `recuperar_contrasena_email.png` - Imagen 2
- [ ] `pago_servicios.png` - Imagen 3
- [ ] `restablecer_contrasena.png` - Imagen 4
- [ ] `contrasena_actualizada.png` - Imagen 5
- [ ] `movimientos.png` - Imagen 6
- [ ] `mis_tarjetas.png` - Imagen 7

## Comandos Después de Guardar

Una vez que hayas guardado todas las imágenes, ejecuta:

```bash
# 1. Compilar la documentación
cd docs
python -m sphinx -b html source build/html

# 2. Agregar cambios a Git
git add .

# 3. Hacer commit
git commit -m "Actualizar manual de usuario con nuevas pantallas"

# 4. Desplegar a GitHub Pages
git push origin main
```

## Verificación

Después del despliegue, verifica que las imágenes se vean correctamente en:
https://joelml1.github.io/documentacion_billcash/

## Notas Importantes

✅ **Formato:** Todas las imágenes deben estar en formato PNG
✅ **Calidad:** Mantén buena resolución para que se vean claras
✅ **Nombres:** Usa exactamente los nombres especificados (minúsculas, guiones bajos)
✅ **Ubicación:** Todas en `docs/source/_static/`

## Nuevas Secciones Creadas

El manual de usuario ahora incluye:

1. ✅ **Manual de Introducción**
2. ✅ **Manual de Registro**
3. ✅ **Manual de Login**
4. 🆕 **Manual de Recuperación de Contraseña**
5. ✅ **Manual de Home/Dashboard**
6. ✅ **Manual de Enviar Dinero**
7. ✅ **Manual de Solicitar Dinero** (actualizado con imagen de estado vacío)
8. ✅ **Manual de Cartera/Movimientos** (actualizado con nueva imagen)
9. 🆕 **Manual de Gestión de Tarjetas**
10. 🆕 **Manual de Pago de Servicios**

---

**Fecha de actualización:** Diciembre 2025
**Versión:** 1.0.0
