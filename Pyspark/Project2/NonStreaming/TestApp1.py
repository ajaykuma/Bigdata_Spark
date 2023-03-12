"""
--refer RunInstructions.txt file--
"""
from pyspark import SparkContext,SparkConf
"""Along with appName, we can add master="local" and define number of threads needed in SparkContext"""
sc = SparkContext(appName="sparkrddex1",master="local[*]")
"""If running on a cluster, comment above line and uncomment below line"""
#sc = SparkContext(appName="TestAppl")

"""Reading file from local machine instead of HDFS path """
"""inputpath = "file:///home/hdu/PycharmProjects/pythonProject/Project2/Data/cv000_29416.txt"
"""

"""Reading file from local machine(windows) instead of HDFS path"""
"""
#inputpath1 = "file:///C:\\Users\\Win10\\Downloads\\Project2\\Data\\cv000_29416.txt"
"""
"""Reading file from HDFS"""
inputpath = "/sampledata/cv000_29416.txt"
x = sc.textFile(inputpath)
print(x.map(lambda n: n.upper()).collect())
