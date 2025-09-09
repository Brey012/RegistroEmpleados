# 💼 Sistema de Gestión de Nómina de Empleados

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Autor-disenoydesarrollo-green.svg" alt="Autor">
  <img src="https://img.shields.io/badge/Año-2025-orange.svg" alt="Año">
</p>

---

## 👤 Autor
- **Nombre:** disenoydesarrollo
- **Año:** 2025

---

## 📋 Descripción
Este proyecto es una aplicación de consola en Python para gestionar empleados y calcular la nómina mensual de una empresa. Permite registrar empleados, ver la lista de empleados, calcular el total de la nómina y eliminar empleados por ID.

---

## ✨ Características principales
- **Registrar empleado:** Permite ingresar los datos de un nuevo empleado (nombre, correo, teléfono, cargo, valor por hora y horas trabajadas).
- **Ver todos los empleados:** Muestra la lista de empleados registrados, su cargo y el salario calculado.
- **Ver el total de la nómina:** Calcula y muestra el costo total de la nómina (suma de los salarios de todos los empleados).
- **Eliminar empleado por ID:** Permite eliminar un empleado usando su ID único.

---

## 🛠️ Estructura del código
- Los empleados se almacenan en una lista de diccionarios, cada uno con los datos del empleado.
- El sistema usa funciones para cada acción principal:
  - `registrar_empleado()`: Registra un nuevo empleado.
  - `ver_todos_los_empleados()`: Muestra la lista de empleados y sus salarios.
  - `ver_total_nomina()`: Calcula y muestra el total de la nómina.
  - `eliminar_empleado_por_id()`: Elimina un empleado por su ID.
- El menú principal permite al usuario seleccionar la acción que desea realizar.

---

## 🚀 Cómo usar el sistema
1. Ejecuta el archivo `main.py` con Python:
   ```powershell
   python main.py
   ```
2. Selecciona una opción del menú:
   - Registrar empleado
   - Ver todos los empleados
   - Ver el total de la nómina
   - Eliminar empleado por ID
   - Salir
3. Sigue las instrucciones en pantalla para cada opción.

---

## 📦 Requisitos
- Python 3.x
- No requiere librerías externas

---

## 📝 Notas
- El sistema almacena los empleados en memoria, por lo que los datos se pierden al cerrar el programa.
- El ID de empleado es autoincremental y único para cada registro.

---

> ¡Puedes modificar el código para agregar nuevas funcionalidades como guardar los datos en un archivo o agregar validaciones adicionales!
