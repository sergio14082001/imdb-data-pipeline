from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType
import os

def main():
    # Inicializar spark session
    spark = SparkSession.builder \
        .appName("IMDb Processing") \
        .config("spark.sql.session.timeZone","UTC") \
        .getOrCreate() # Si no existe, crea una nueva sesión de Spark. Si ya existe una, la reutiliza.


    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    output_path1 = os.path.join(base_dir, f"title.basics.tsv.gz")
    output_path2 = os.path.join(base_dir, f"title.ratings.tsv.gz")

    # Leer el archivo title.basics.tsv.gz
    df_basics = spark.read.option("header",True) \
                .option("sep","\t") \
                .option("nullValue","\\N") \
                .csv(f"{output_path1}")

    # Primera fila son cabeceras
    # Separador de campos es tabulador
    # Convierte los \N en nulls



    # Mostrar el esquema y algunas filas
    df_basics.printSchema()
    df_basics.show(5)

    # Guardar como Parquet
    #df_basics.write.mode("overwrite").parquet("../data/processed/title_basics.parquet")
    df_basics.write.mode("overwrite").parquet("/opt/airflow/dags/data/processed/title_basics.parquet") 
    


    # -------------------
    # Leer title.ratings.tsv.gz
    # -------------------

    schema_ratings = StructType([
        StructField("tconst", StringType(), True),
        StructField("averageRating", FloatType(), True),
        StructField("numVotes", IntegerType(), True)
    ])


    df_ratings = spark.read.option("header", True) \
                .option("sep","\t") \
                .schema(schema_ratings) \
                .csv(f"{output_path2}")

    #df_ratings.write.mode("overwrite").parquet("../data/processed/title_ratings.parquet")
    df_ratings.write.mode("overwrite").parquet("/opt/airflow/dags/data/processed/title_ratings.parquet")

    spark.stop() # Detener la sesión de Spark

if __name__ == "__main__":
    main()
