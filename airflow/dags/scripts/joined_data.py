from pyspark.sql import SparkSession

def main():

        # Crear la sesion de spark
        spark = SparkSession.builder \
                .appName("IMDB Join Data") \
                .getOrCreate()

        # Leer los archivos parquet procesados
        df_basics = spark.read.parquet("/opt/airflow/dags/data/processed/title_basics.parquet")
        df_ratings = spark.read.parquet("/opt/airflow/dags/data/processed/title_ratings.parquet")

        # Realizar el join usando la clave primaria 'tconst'
        df_joined = df_basics.join(df_ratings, on="tconst", how="inner")

        # Guardar resultado del join
        df_joined.write.mode("overwrite").parquet("/opt/airflow/dags/data/processed/title_joined.parquet")

        # Cerrar sesion de spark
        spark.stop()

if __name__ == "__main__":
    main()