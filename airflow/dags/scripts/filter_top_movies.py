from pyspark.sql import SparkSession

def main():

    # Crear la sesion de spark
    spark = SparkSession.builder \
            .appName("IMDB Join Data") \
            .getOrCreate()

    # Leer datos combinados
    df_joined = spark.read.parquet("/opt/airflow/dags/data/processed/title_joined.parquet")

    # Filtrar peliculas con buen rating
    df_filtered = df_joined.filter(
        (df_joined["titleType"] == "movie") &
        (df_joined["averageRating"] >= 8.0) &
        (df_joined["numVotes"] >= 50000)
    )

    # Guardar resultados
    df_filtered.write.mode("overwrite").parquet("/opt/airflow/dags/data//processed/top_movies.parquet")

    # Cerrar sesion de spark
    spark.stop()

if __name__ == "__main__":
    main()