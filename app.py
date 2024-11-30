from flask import Flask, render_template
import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go
import json
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)

# Resolver la ecuación diferencial
def solve_differential():
    # Ejemplo: y' = -2y + t
    def equation(t, y):
        return -2 * y + t

    t_span = (0, 5)  # Intervalo de tiempo
    y0 = [1]         # Condición inicial
    t_eval = np.linspace(t_span[0], t_span[1], 100)  # Puntos para evaluar
    solution = solve_ivp(equation, t_span, y0, t_eval=t_eval)

    return solution.t, solution.y[0]

@app.route('/')
def index():
    t, y = solve_differential()
    # Crear el gráfico interactivo con Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name="y(t)"))
    fig.update_layout(title="Gráfico de la ecuación diferencial", 
                      xaxis_title="t", 
                      yaxis_title="y(t)")
    
    # Convertir el gráfico a JSON para pasar al frontend
    graph_json = json.dumps(fig, cls=PlotlyJSONEncoder)
    return render_template('index.html', graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True)
