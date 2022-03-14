from pyspark import SparkConf, SparkContext
sc = SparkContext(master="local[1]",appName="RDDAppl")
inputpath = "Data2"
x = sc.textFile("Data2\\cv000_29416.txt")
y = x.flatMap(lambda n: n.split(" "))
z = y.map(lambda n: (n,1))
for i in z.take(10):
    print(i)