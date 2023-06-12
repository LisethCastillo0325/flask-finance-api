# Este script en Python ejemplifica como desde el lenguaje Python se pueden
# enviar peticiones a nuestra aplicacion
import requests

URL = "http://localhost:5000/consultar_accion"

FECHA_INICIAL = "2020-01-01"
FECHA_FINAL = "2021-01-01"

# Envio peticion 'GET'
response = requests.get(URL, json={"accion": "GOOGL", "fecha_inicial": FECHA_INICIAL, "fecha_final": FECHA_FINAL})
print("Respuesta a GET")
# Imprimir los datos de la respuesta como cadena de texto
print(response.content.decode('utf-8'))
input("Presione ENTER para continuar...")

