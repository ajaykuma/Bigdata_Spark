"""Broadcast variable example1"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
spark = SparkSession.builder\
    .appName("sparkrddex2")\
    .master("local[*]")\
    .getOrCreate()

accum=spark.sparkContext.accumulator(0)
rdd=spark.sparkContext.parallelize([1,2,3,4,5])
rdd.foreach(lambda x:accum.add(x))
"""rdd.foreach() is executed on workers and accum.value is called from PySpark driver program."""
print(accum.value) #Accessed by driver

"""Using a function"""
accuSum=spark.sparkContext.accumulator(0)
def countFun(x):
    global accuSum
    accuSum+=x
rdd.foreach(countFun)
print(accuSum.value)

"""Using accumulators to do counters"""
accumCount=spark.sparkContext.accumulator(0)
rdd2=spark.sparkContext.parallelize([1,2,3,4,5])
rdd2.foreach(lambda x:accumCount.add(1))
print(accumCount.value)
