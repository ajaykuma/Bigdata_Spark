""" Non Streaming example:
--refer RunInstructions.txt file--
"""
"""Reading different file formats"""

from pyspark.sql import SparkSession
spark = SparkSession.builder\
    .appName("sparkdfex1")\
    .master("local[*]")\
    .getOrCreate()

"""Remove --> .master("local") above to run on YARN"""
"""Reading file from local machine(windows) instead of HDFS path """
"""inputpath = "file:///C:\\Users\\Win10\\Downloads\\Project2\\Data\\people.json"
"""

"""Reading file from local machine instead of HDFS path """
"""inputpath = "file:///home/hdu/PycharmProjects/pythonProject/Project2/Data/people.json"
"""

"""Reading file from HDFS"""
inputpath1 = "/sampledata/people.json"
inputpath2 = "/sampledata/recipes.json"
inputpath3 = "/sampledata/Bank_full.csv"

"""inputDF = spark.read.json(inputpath1)"""
inputDF1 = spark.read.format("json").load(inputpath1)
inputDF1.show(2)
inputDF1.printSchema()
print(inputDF1.count())

inputDF2 = spark.read.format("json").option("inferSchema","true").load(inputpath2)
"""inputDF2 = spark.read.format("json").load(inputpath2)"""
inputDF2.show(2)
inputDF2.printSchema()
print(inputDF2.count())

inputDF3 = spark.read.format("json").load(inputpath2,multiLine=True)
inputDF3.show(2)
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

