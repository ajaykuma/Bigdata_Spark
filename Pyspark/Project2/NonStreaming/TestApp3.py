""" Non-Streaming example, passing in a schema instead of infer schema
--refer RunInstructions.txt file--
"""
"""Reading different file formats"""

from pyspark.sql.types import IntegerType,StringType, StructType, StructField
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("sparkdfex").getOrCreate()
inputpath = "file:///C:\\Users\\Win10\\Downloads\\Project2\\Data"
schema = StructType([StructField("name",StringType(),True),
                     StructField("age",IntegerType())])

inputDF = (spark.read.schema(schema).json(inputpath))

inputDF.show()
inputDF.printSchema()
print(inputDF.count())