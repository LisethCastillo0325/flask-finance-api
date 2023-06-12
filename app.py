"""
Daniel Caicedo
Liseth Castillo 
"""

from datetime import datetime

# Flas
from flask import Flask, request

# script
from script import get_stock_data

# Inicialización flask
app = Flask(__name__)


@app.route('/consultar_accion', methods=['POST'])
def test():
    data = request.get_json()
    ticker = data['accion']
    start_date = data['fecha_inicial']
    end_date = data['fecha_final']
    datos_accion = get_stock_data(start_date, ticker, end_date)
    ultimos_registros = datos_accion.tail()    
    # Convertir los datos a un formato JSON
    respuesta = ultimos_registros.to_json(orient='index')
    return respuesta


if __name__ == "__main__":
    print(f"{datetime.now()}")
    app.run(host='0.0.0.0',debug=True)
