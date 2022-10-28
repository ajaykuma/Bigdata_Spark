""" Non Streaming example:
--refer RunInstructions.txt file--
"""
"""Reading different file formats"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.\
    appName("sparkdfex").\
    getOrCreate()


inputpath1 = "file:///C:\\Users\\Win10\\Downloads\\Project2\\Data"
inputpath2 = "file:///C:\\Users\\Win10\\Downloads\\Project2\\Data2"
inputpath3 = "file:///C:\\Users\\Win10\\Downloads\\Project2\\Data4"

"""inputDF = spark.read.json(inputpath1)"""
inputDF1 = spark.read.format("json").load(inputpath1)
inputDF1.show()
inputDF1.printSchema()
print(inputDF1.count())

inputDF2 = spark.read.format("json").load(inputpath2)
"""inputDF2 = spark.read.format("json").option("inferSchema","true").load(inputpath2)"""
inputDF2.show(5)
inputDF2.printSchema()
print(inputDF2.count())

inputDF3 = spark.read.format("json").load(inputpath2,multiLine=True)
inputDF3.show()
inputDF3.printSchema()
print(inputDF3.count())

inputDF4 = spark.read.csv(inputpath3)
inputDF4.show(2)
print(inputDF4.count())
inputDF4 = spark.read.format("csv").option("header","true").option("inferSchema","true").option("delimiter",",").\
           load(inputpath3)
inputDF4.show(3)
print(inputDF4.count())

inputDF4.printSchema()

