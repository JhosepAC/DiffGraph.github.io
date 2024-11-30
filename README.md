# Gráfico de Ecuación Diferencial

Este proyecto es una aplicación web desarrollada con Flask que resuelve una ecuación diferencial ordinaria (EDO) y muestra el gráfico interactivo de la solución utilizando Plotly.

## Características

- Resuelve ecuaciones diferenciales ordinarias usando la librería **SciPy**.
- Genera gráficos interactivos con **Plotly**.
- Implementa un diseño web minimalista y responsivo utilizando **HTML** y **CSS**.
- Diseñado para ser fácil de entender y extender.

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/TuUsuario/differential-equation-graph.git
   cd differential-equation-graph
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

5. Abre tu navegador y ve a [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Librerías Utilizadas

Las principales librerías utilizadas en este proyecto son:

1. **Flask**: Framework para crear aplicaciones web ligeras en Python.
2. **NumPy**: Para realizar cálculos matemáticos.
3. **SciPy**: Para resolver ecuaciones diferenciales ordinarias.
4. **Plotly**: Para crear gráficos interactivos.
5. **Jinja2**: Motor de plantillas para renderizar HTML dinámico (integrado con Flask).

---

## Qué Hace el Programa

1. Resuelve una ecuación diferencial ordinaria, por ejemplo:
   \[
   y' = -2y + t
   \]
   con la condición inicial \( y(0) = 1 \).

2. Calcula la solución en un intervalo definido (\([0, 5]\)).

3. Genera un gráfico interactivo de la solución \( y(t) \) contra \( t \).

4. Muestra el gráfico en una interfaz web minimalista y responsiva.

---

## Archivos Principales

- **app.py**: Archivo principal de la aplicación Flask.
- **templates/index.html**: Plantilla HTML para renderizar la interfaz web.

---

## Autor

Desarrollado por Jhosep Argomedo.