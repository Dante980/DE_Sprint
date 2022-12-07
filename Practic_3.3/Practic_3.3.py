from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType,  StringType, TimestampType, BooleanType, DateType
from pyspark.sql.functions import lit

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('PySpark_Tutorial') \
    .getOrCreate()

schema = StructType(fields=[
    StructField("id", IntegerType()),
    StructField("timestemp", IntegerType()), # TimestampType()
    StructField("type", StringType()),  # "visit", "click", "scroll", "move"
    StructField("page_id", IntegerType()),
    StructField("tag", StringType()),   # "Politika", "Sport", "Medicina", "Priziv"
    StructField("sing", BooleanType())
])

df = spark.read.csv("input_data.csv", schema=schema, sep="|")
# # input_data.csv
# 1|1667627426|"click"|101|"Sport"|True
# 2|1667627427|"click"|102|"Politika"|False
# 3|1667627428|"click"|102|"Politika"|False
# 2|1667627429|"click"|102|"Politika"|False
# 4|1667627430|"click"|103|"Medicina"|False
# 3|1667627431|"click"|104|"Priziv"|False
# 4|1667627432|"click"|105|"Priziv"|False
# 3|1667627433|"scroll"|105|"Priziv"|False
# 4|1667627434|"click"|106|"Medicina"|False
# 3|1667627435|"click"|105|"Priziv"|False
# 4|1667627435|"click"|105|"Priziv"|False
# 3|1667627436|"scroll"|105|"Priziv"|False

df.show(5, vertical=True, truncate=False)
# # task 1-2


df_temp = df.groupBy("sing")
count_ = df.count()
temp_temp = df_temp\
    .rdd\
    .map(lambda x:
                     (x[0], x[1] / count_ * 100)
         ) \
    .toDF()
temp_temp.show()
# task 3


df_temp = df.groupBy("page_id", "type").count().drop("page_id").groupBy("type").mean()
df_temp.show(1)
# task 4

df_temp = df.withColumn("NewColl", lit(""))
df_temp.show()
# task 5





# task 6







# task 7
schema = StructType(fields=[
    StructField("id", IntegerType()),
    StructField("User_id", IntegerType()),
    StructField("Users_FIO", StringType()),
    StructField("Creation_date", StringType())
])
# # input_user_data.csv
# 1|1|"Shpak Valentin Ivanovich"|"21.11.1999"
# 2|2|"Mizantropov Anatoli Manevich"|"21.11.2023"
# 3|3|"Saveliev Maksim Karpovich"|"21.11.2021"
# 4|4|"Dekterev Evgeni Hazarovich"|"22.11.2022"


users_df = spark.read.csv("input_user_data.csv", schema=schema, sep="|")
users_df.show()
# task 8
df_temp = users_df.join(df, users_df.User_id == df.id, how="inner").drop("id")
df_temp.show()


# task 9
df_temp.where(df_temp.tag == "Sport").groupBy("Users_FIO").count().drop("count").show()

