# Instrucciones de ejecución

## Usando entorno virtual de python

### Crear entorno virtual

`python3 -m venv venv`

### Activar entorno virtual

`source venv/bin/activate`

### Instalar dependencias

`pip install -r requirements.txt`

### Correr webservice

`python3 app.py`

## Usando Docker

### Compilar imagen

`docker image build -t zethoc/stock-market:1.0 .`


### Ejecutar contenedor

`docker container run --rm --name stock-market -p 5000:5000 zethoc/stock-market:1.0`



# Ejemplo acceso o consumo de endpoint "consultar_accion"

### CURL

`curl -X GET -H 'Content-type: application/json' -d '{"accion": "GOOGL", "fecha_inicial": "2020-01-01", "fecha_final": "2022-01-01"}' http://localhost:5000/consultar_accion`


### Python

`python3 requests_example.py`
