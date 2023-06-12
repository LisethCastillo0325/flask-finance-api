"""
Daniel Caicedo
Liseth Castillo 
"""

# Flas
from flask import Flask, request

# Importing the yfinance package
import yfinance as yf


app = Flask(__name__)
def get_stock_data(sd, stock, ed):
    return yf.download(stock, sd, ed)


@app.route('/consultar_accion', methods=['GET'])
def test():
    data = request.get_json()
    ticker = data['accion']
    start_date = data['fecha_inicial']
    end_date = data['fecha_final']
    datos_accion = get_stock_data(start_date,ticker,end_date)
    ultimos_registros = datos_accion.tail()    
    # Convertir los datos a un formato JSON
    respuesta = ultimos_registros.to_json(orient='index')
    return respuesta


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
