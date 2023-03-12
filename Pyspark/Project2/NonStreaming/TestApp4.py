"""Broadcast variable example1"""
import pyspark
from pyspark.sql import SparkSession
"""from pyspark.sql.functions import col, lit, udf"""
from pyspark.sql.functions import udf
spark = SparkSession.builder\
    .appName("sparkdfex6")\
    .master("local[*]")\
    .getOrCreate()


country = dict({'AK': 'Alaska', 'AL': 'Alabama'})
brod = spark.sparkContext.broadcast(country)
def getvalue(cid):
    if cid in country:
        return brod.value[cid]

"""If not using brodcast ,comment out brod and modify function as below"""
"""def getvalue(cid):
    if cid in country:
        return country.get(cid)"""

testudf = udf(getvalue)

read_data = spark.read.format("csv").option("header", "True"). \
    load("/sampledata/world_country_and_usa_states_latitude_and_longitude_values.csv")

read_data.printSchema()
final_df = read_data.withColumn("brod_country", testudf("usa_state_code"))
final_df.show(2)
#read_data.show()


