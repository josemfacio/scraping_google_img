# Script de Descarga y Actualización de Imágenes

Este script descarga imágenes de Google Images basadas en palabras clave proporcionadas y actualiza el campo de imagen en una API de servidor.

## Uso

1. Instala las dependencias requeridas: `pip install requests progressbar2 python-magic`
2. Configura los parámetros necesarios, como la URL del servidor y el token de autorización.
3. Ejecuta el script: `python image_download.py`

## Descripción

El script `image_download.py` se utiliza para buscar imágenes en Google Images basadas en palabras clave proporcionadas. Utiliza la biblioteca `requests` para enviar solicitudes HTTP y descargar las imágenes. Las imágenes descargadas se actualizan en la API del servidor mediante una solicitud PATCH.

El script maneja interrupciones en el proceso de descarga de imágenes mediante el seguimiento del índice actual. Esto permite que el script reanude la descarga desde el punto donde se detuvo.

Las imágenes descargadas se almacenan en un directorio local especificado. El script también utiliza la biblioteca `progressbar2` para mostrar una barra de progreso durante el proceso de descarga de imágenes.

## Requisitos

- Python 3.x
- requests
- progressbar2
- python-magic

## Licencia

Este script está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.




# English




# Image Download and Update Script

This script downloads images from Google Images based on provided keywords and updates the image field in a server API.

## Usage

1. Install the required dependencies: `pip install requests progressbar2 python-magic`
2. Set the necessary parameters such as the server URL and authorization token.
3. Run the script: `python image_download.py`

## Description

The script `image_download.py` is used to search for images on Google Images based on provided keywords. It utilizes the `requests` library to send HTTP requests and download the images. The downloaded images are then updated in the server's API by sending a PATCH request.

The script handles interruptions in the image downloading process by keeping track of the current index. This allows the script to resume downloading from the point where it stopped.

The downloaded images are stored in a specified local directory. The script also uses the `progressbar2` library to display a progress bar during the image downloading process.

## Requirements

- Python 3.x
- requests
- progressbar2
- python-magic

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
