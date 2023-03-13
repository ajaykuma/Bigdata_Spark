"""Broadcast variable example1"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
spark = SparkSession.builder\
    .appName("sparkdfex4")\
    .master("local[*]")\
    .getOrCreate()


states = dict({"NY":"New York","CA":"California","FL":"Florida"})
countries = dict({"USA":"United States of America","IN":"India"})


broadcastStates = spark.sparkContext.broadcast(states)
broadcastCountries = spark.sparkContext.broadcast(countries)

data = [("James", "Smith", "USA", "CA"), ("Michael", "Rose", "USA", "NY"), ("Robert", "Williams", "USA", "CA"),
        ("Maria", "Jones", "USA", "FL")]

rdd = spark.sparkContext.parallelize(data)

def fu(x):
  country = x[2]
  state = x[3]
  fullCountry = broadcastCountries.value[country]
  fullState = broadcastStates.value[state]
  return [x[0],x[1],fullCountry,fullState]

rdd2 = rdd.map(lambda n : fu(n))
print(rdd2.collect())


