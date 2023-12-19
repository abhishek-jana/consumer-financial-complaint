from pyspark.sql import SparkSession

# spark_session = SparkSession.builder.master('local[*]').appName('finance_complaint').getOrCreate()

spark_session = SparkSession.builder.master('local[*]').appName('finance_complaint') \
    .config("spark.executor.instances", "4") \
    .config("spark.executor.memory", "16g") \
    .config("spark.driver.memory", "16g") \
    .config("spark.executor.memoryOverhead", "16g") \
    .getOrCreate()