"""Broadcast variable example1"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
spark = SparkSession.builder\
    .appName("sparkdfex6")\
    .master("local[*]")\
    .getOrCreate()


