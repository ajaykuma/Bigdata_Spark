from pyspark import SparkContext,SparkConf
sc = SparkContext(master="local",appName="TestAppl")
inputpath = "Data"

x = sc.textFile(inputpath)
x.map(lambda n: n.upper()).collect()
