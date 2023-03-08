"""
--refer RunInstructions.txt file--
"""
from pyspark import SparkContext,SparkConf
sc = SparkContext(appName="TestAppl")
"""Along with appName, we can add master="local" and define number of threads needed in SparkContext"""
"""Reading file from local machine instead of HDFS path or set the input path accordingly"""
inputpath = "file:///C:\\Users\\Win10\\Downloads\\Project2\\Data"

x = sc.textFile(inputpath)
print(x.map(lambda n: n.upper()).collect())
