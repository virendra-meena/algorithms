from pyspark.sql.session import SparkSession

spark = SparkSession.builder \
        .master('local') \
        .appName('word count') \
        .config("key", "value") \
        .getOrCreate()


df = spark.createDataFrame()