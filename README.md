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
Docker | Contenedores
Apache Airflow |	Orquestación de pipelines
Git & GitHub |	Control de versiones

---

🚀 Descarga de Datos <br/>

Este proceso se encarga de:

1. Conectarse al portal oficial de IMDb Datasets.

2. Descargar los archivos comprimidos:

   - title.basics.tsv.gz
   
   - title.ratings.tsv.gz

3. Guardarlos en la carpeta local dags/data/.

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

🛫 Orquestación del pipeline con Apache Airflow

En la etapa final del proyecto, se utilizó Apache Airflow para automatizar el flujo de trabajo completo, desde la descarga de datos hasta el procesamiento y almacenamiento final. Esta es una práctica común en entornos productivos donde se requiere que los pipelines se ejecuten de forma recurrente y controlada.

📂 Estructura de archivos relevante

```
Airflow/
├── dags/
│   ├── imdb_pipeline_dag.py      # DAG principal del proyecto
│   ├── data/                     # Archivos .tsv.gz y carpeta processed/
│   └── scripts/                  # Scripts Python utilizados en cada tarea
├── docker-compose.yaml          # Configuración de servicios Airflow
├── Dockerfile                   # Instalación de dependencias adicionales
├── plugins/
└── logs/
```

⚙️ Configuración del entorno con Docker

Se utilizó Docker para levantar todos los servicios necesarios de Airflow:

- Webserver: Interfaz web de monitoreo.

- Scheduler: Encargado de programar y ejecutar tareas.

- Postgres: Base de datos backend para almacenar metadatos.

(No se utilizaron workers ni Celery, dado que se usó el SequentialExecutor por simplicidad.)


```
# Desde la carpeta Airflow/
docker-compose up -d
```

Una vez levantado, puedes acceder a la interfaz de Airflow en:

```
http://localhost:8080
```

Credenciales por defecto:

- Usuario: airflow

- Contraseña: airflow

---

📌 DAG: imdb_pipeline_dag

El DAG imdb_pipeline_dag.py define las siguientes tareas:

1. Descargar datos: Ejecuta download_data.py.

2. Procesar datos: Ejecuta process_data.py.

3. Unir datasets: Ejecuta joined_data.py.

4. Filtrar top películas: Ejecuta filter_top_movies.py.

Cada tarea se ejecuta de forma secuencial, y los resultados finales se almacenan en formato Parquet dentro de la carpeta data/processed/.

---

📌 Próximos pasos y mejoras sugeridas

- 🌍 Publicar el dashboard final en Power BI Service o Tableau Public.

---

🙋 Autor

**Sergio Sánchez**  
Ingeniero de Sistemas con enfoque en ingeniería de datos y visualización.  
[LinkedIn](www.linkedin.com/in/sergio-sanchez-rojas-161728208) | [GitHub](https://github.com/sergio14082001)

---
