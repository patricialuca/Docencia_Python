# 🚀 PROYECTO ARTEMISA: El Regreso a la Luna

La humanidad se prepara para volver a la Luna, esta vez para quedarse. Nuestra clase ha sido seleccionada para desarrollar el software de control de la nave Orion.

Como el sistema es complejo, utilizaremos **Programación Modular**: dividiremos el problema en pequeños archivos especializados que se unirán en un ordenador central.

## 📂 Arquitectura del Sistema

El software consta de 5 archivos trabajando en conjunto en la misma carpeta:

* `main.py`: **Programa Principal**. Solicita datos, llama a los expertos y toma decisiones.
* `seguridad.py`: Responsable del control de acceso.
* `clima.py`: Responsable de evaluar las condiciones atmosféricas.
* `motor.py`: Responsable de los cálculos de combustible.
* `fisica.py`: Responsable de calcular tiempos de trayectoria.

---

## ⚙️ Flujo del Programa (main.py)

El ordenador central sigue este guion de 4 fases:

1.  **FASE 1: Autenticación.** Solicita contraseña y verifica con el módulo de seguridad. Si falla, el sistema se apaga.
2.  **FASE 2: Chequeo Atmosférico.** Solicita velocidad del viento y lluvia. Si el módulo de clima indica peligro, se aborta la misión.
3.  **FASE 3: Planificación.** Solicita distancia, peso y velocidad. Calcula combustible y tiempo de vuelo usando los módulos de motor y física.
4.  **FASE 4: Lanzamiento.** Muestra el resumen de la misión y ejecuta la cuenta atrás.

---

## 🛠️ Especificaciones de los Módulos

### GRUPO 1: Departamento de Propulsión (`motor.py`)
* **Función:** `calcular_combustible(distancia, peso)`
* **Lógica:**
    * Consumo base = `(distancia * peso) / 500`
    * Si el peso > 5000 kg, el consumo aumenta un 50% extra.
* **Retorno:** Litros de combustible (float).

### GRUPO 2: Departamento de Meteorología (`clima.py`)
* **Función:** `es_seguro_lanzar(velocidad_viento, esta_lloviendo)`
* **Lógica:**
    * Seguro solo si `velocidad_viento < 30` Y `esta_lloviendo == "no"`.
* **Retorno:** `True` (seguro) o `False` (peligro).

### GRUPO 3: Departamento de Física (`fisica.py`)
* **Función:** `tiempo_llegada(distancia, velocidad)`
* **Lógica:**
    * Fórmula: `Tiempo = Distancia / Velocidad`
    * *Nota: Si velocidad es 0, devuelve 0 para evitar errores.*
* **Retorno:** Horas de viaje (float).

### GRUPO 4: Departamento de Seguridad (`seguridad.py`)
* **Función:** `verificar_codigo(codigo_ingresado)`
* **Lógica:**
    * Compara el código con la contraseña maestra: `"MARTE2025"`.
* **Retorno:** `True` (correcto) o `False` (incorrecto).

---
¡Buena suerte, ingenieros! 🌕
