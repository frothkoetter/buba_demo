from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CDE FIRST STEPS").getOrCreate()

S3_BUCKET = "s3a://go01-demo/data/landing/"

sales_df_2021 = spark.read.csv(f"{S3_BUCKET}/data/2021/sales.csv", header=True, inferSchema=True)
sales_df_2021.show()

sales_df_2022 = spark.read.csv(f"{S3_BUCKET}/data/2022/sales.csv", header=True, inferSchema=True)
sales_df_2022.show()
