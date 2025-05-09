# 🎬 IMDb Data Pipeline Project 

Este proyecto de Ingeniería de Datos tiene como objetivo construir un pipeline de datos que descarga, transforma y almacena información proveniente del IMDb Datasets, utilizando herramientas comúnmente utilizadas en el stack de un Data Engineer.

📌 Objetivos del proyecto
Descargar datos reales del portal IMDb (archivos .tsv.gz).

- Limpiar y transformar los datos utilizando PySpark.

- Almacenar los resultados en formato Parquet y Delta Lake.

- Automatizar el pipeline con Apache Airflow (fase final).

- Construir un portafolio técnico sólido con herramientas reales.

🧰 Tecnologías utilizadas
Herramienta |	Propósito
|-|-|
Python |	Programación principal
PySpark |	Procesamiento distribuido
Delta Lake |	Almacenamiento confiable
Apache Airflow |	Orquestación de pipelines
Git & GitHub |	Control de versiones

---

🚀 Cómo ejecutar el script de descarga de datos <br/>

Sigue estos pasos para ejecutar el script download_data.py dentro del entorno virtual del proyecto:

1. Clonar el repositorio (si aplica)<br/>
```
git clone https://github.com/tu-usuario/imdb-data-pipeline.git
cd imdb-data-pipeline
```

2. Crear y activar el entorno virtual (solo la primera vez)<br/>
```
python -m venv venv
# Activar entorno:
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```
3. Instalar dependencias<br/>
```
pip install -r requirements.txt
```
4. Ejecutar el script de descarga<br/>
```
python scripts/download_data.py
```
5. (Opcional) Desactivar entorno virtual<br/>
```
deactivate
```
---

📊 Procesamiento y transformación de datos

Luego de la descarga, los archivos `.tsv.gz` fueron procesados con PySpark. A continuación se detallan los pasos realizados:

1. **Lectura de archivos brutos**:  
   - `title.basics.tsv.gz`: Información básica de títulos.  
   - `title.ratings.tsv.gz`: Calificaciones y cantidad de votos.

2. **Transformación de datos**:  
   - Se aplicaron filtros para seleccionar únicamente películas (`titleType == 'movie'`).
   - Se eliminaron valores nulos en campos críticos como `primaryTitle` y `startYear`.
   - Se unieron los datasets mediante el campo `tconst`.

3. **Exportación en formatos eficientes**:  
   - Los resultados fueron almacenados en formato **Parquet**, optimizando lectura y almacenamiento.

---

📈 Visualización con Power BI

Se diseñó un **dashboard interactivo en Power BI** a partir de los datos transformados, cargando los archivos Parquet del conjunto final (`TOP_MOVIES`).  
Este dashboard permite:

- Visualizar películas con mayor rating y mayor número de votos.
- Filtrar por años de estreno.
- Explorar tendencias en calificación y producción cinematográfica.

> ✅ Todos los archivos `.parquet` fueron importados exitosamente desde una carpeta, usando la opción **"Carpeta"** en Power BI para combinar múltiples archivos en una sola tabla.

---

📌 Próximos pasos y mejoras sugeridas

- 🔄 **Automatizar el pipeline con Apache Airflow**.
- 🎭 Incluir otros datasets de IMDb como `name.basics`, `title.crew`, `title.principals` para enriquecer el análisis.
- 🧠 Calcular un ranking ponderado usando una fórmula basada en `numVotes` y `averageRating`.
- 🌍 Publicar el dashboard final en Power BI Service o Tableau Public.

---

🙋 Autor

**Sergio Sánchez**  
Ingeniero de Sistemas con enfoque en ingeniería de datos y visualización.  
[LinkedIn](www.linkedin.com/in/sergio-sanchez-rojas-161728208) | [GitHub](https://github.com/sergio14082001)

---