# README

Este documento describe los pasos para crear un entorno virtual (venv) y configurar una aplicación básica de Flask con una pequeña ruta.

## Requisitos previos

- Python instalado en tu sistema.

## Creación del entorno virtual

1. Abre una terminal y navega al directorio de tu proyecto:
    ```sh
    cd /c:/Users/XXXX/XXXX/XXXX
    ```

2. Crea un entorno virtual:
    ```sh
    python -m venv venv
    ```

3. Activa el entorno virtual:
    - En Windows:
        ```sh
        venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

## Instalación de Flask

1. Con el entorno virtual activado, instala Flask:
    ```sh
    pip install Flask
    ```

## Creación de una aplicación Flask básica

1. Crea un archivo `app.py` en el directorio de tu proyecto con el siguiente contenido:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "¡Hola, Flask!"

    if __name__ == '__main__':
        app.run(debug=True)
    ```

2. Ejecuta la aplicación Flask:
    ```sh
    python app.py
    ```

3. Abre tu navegador web y navega a `http://127.0.0.1:5000/` para ver la ruta básica.
o lanza el siguiente curl:
    curl -i GET -w '\n' localhost:5000 
