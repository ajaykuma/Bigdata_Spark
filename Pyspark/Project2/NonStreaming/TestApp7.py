""" Non Streaming example:
--refer RunInstructions.txt file--
"""
"""Reading different file formats"""

from pyspark.sql import SparkSession
spark = SparkSession.builder\
    .appName("sparkdfex5")\
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
inputpath = "/sampledata/Bank_full.csv"

inputDF = spark.read.format("csv").option("header","true").option("inferSchema","true").option("delimiter",",").\
           load(inputpath)
inputDF.show(3)
inputDF.printSchema()

