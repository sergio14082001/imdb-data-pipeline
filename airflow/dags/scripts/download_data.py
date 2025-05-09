
import requests #Libreria para hacer peticiones HTTP
import os


def download_file(url, output_path):
    response = requests.get(url) # Realiza la petición HTTP
    with open(output_path, 'wb') as file: # Abre el archivo de salida en modo binario
        file.write(response.content) # Escribe el contenido de la respuesta en el archivo


def main():

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    urls = {
        "title.basics": "https://datasets.imdbws.com/title.basics.tsv.gz",
        "title.ratings": "https://datasets.imdbws.com/title.ratings.tsv.gz"
    }

    for name, url in urls.items():
        output_path = os.path.join(base_dir, f"{name}.tsv.gz")
        print(f"Downloading {name}...")
        download_file(url, output_path)

# Esto asegura que el script también funcione si lo ejecutas directamente
if __name__ == "__main__":
    main()