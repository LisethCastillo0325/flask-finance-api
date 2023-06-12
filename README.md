# Instrucciones

## Crear entonro virtual

`python3 -m venv venv`

## Activar entorno virtual

`source venv/bin/activate`

## Instalar dependencias

`pip install -r requirements.txt`

# Levantar webservice

`python3 app.py`


# Ejemplo Ejecución

## CURL

`curl -X GET -H 'Content-type: application/json' -d '{"accion": "GOOGL", "fecha_inicial": "2020-01-01", "fecha_final": "2022-01-01"}' http://localhost:5000/consultar_accion`


## Python

`python3 requests_example.py`
