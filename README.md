# 🎬 Biblioteca de Películas

Proyecto web desarrollado con Django para la gestión de películas, realizado por Enzo Costamagna.

---

## 📌 Descripción

Este sistema permite administrar una base de datos de películas a través de una interfaz web. Permite gestionar un catálogo de películas: crear, editar, listar y eliminar películas, incluyendo la carga de imágenes. Incluye soporte para:

- Subida y visualización de imágenes (posters).
- CRUD completo (Crear, Leer, Actualizar, Eliminar).
- Gestión desde el panel de administración de Django.
- Una breve descripción sobre mí.
- La posiblidad de registrar y logear usuarios propios.
---

## 🔧 Tecnologías utilizadas

- Python
- Django
- SQLite
- Pillow
- HTML / CSS
- Bootstrap

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/EnzoCosta3524/TuPrimeraPagina-Costamagna.git
```

### 2. Activar el entorno virtual
```bash
.venv\scripts\activate
```

### 3. Ejecutar página web
```bash
cd src
#Nos posicionamos en la ruta raíz para poder ejecutar el siguente comando.

python manage.py runserver 
# Con este comando iniciamos el servidor web.
```

### 4. Acceder al panel de administración
```bash
localhost/admin
#Colocamos esta ruta en el navegador, aca se encuentra el panel de administración.

"Usuario": admin
"Clave": 123
#Estas son las credenciales para entrar al panel.
```
--- 

## Futuras Actualizaciones
La interfaz aún tiene mucho que mejorar cosas como la vista de "cerrar sesion" o los inputs de los formularios que se ven en blanco. La próxima actualización se centrará en arreglar errores visuales hacer más accesible la edición de otros modelos.

---
## Link de video informativo
https://youtu.be/aNKwbeo6U2U