package main.scala

import org.apache.spark.SparkContext 
import org.apache.spark.SparkContext._ 
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql
import org.apache.spark.sql.types._
import org.apache.spark.sql.Row

object FsixthApp extends App {
val conf = new SparkConf().setAppName("HelloSpark").setMaster("local").set("spark.debug.maxToStringFields","100")
//val conf = new SparkConf().setAppName("HelloSpark").set("spark.debug.maxToStringFields","100")
val sc = new SparkContext(conf)
//val fileInfoFile_with_Marked_Data = args(0)
val fileInfoFile_with_Marked_Data = "DataFile2-marked-data.txt"

val x = sc.textFile(fileInfoFile_with_Marked_Data)
val sample1 = x
val newDS = sample1.zipWithIndex().map{case(line,i)=>i.toString + "," + line}
val pairx = newDS.map(x => (x.split(",")(0),x))

//val fileInfoFile_without_Marked_Data = args(1)
val fileInfoFile_without_Marked_Data = "DataFile1-without-marked-data.txt"

val y = sc.textFile(fileInfoFile_without_Marked_Data)
val sample2 = y
val newDS2 = sample2.zipWithIndex().map{case(line,i)=>i.toString + "," + line}
val pairy = newDS2.map(x => (x.split(",")(0),x))

val pairz = pairx.subtract(pairy)

print("Metadata in this file is as follows")
pairy.take(12).foreach(println)

//val outputPath = args(2)
val outputPath = "/home/hdu/workspace/SparkApps/TestOut"
pairz.sortByKey(true).saveAsTextFile(outputPath)

val DataNeeded = "pedestrian"
val x1 = sc.textFile(outputPath + "/" + "part-00000").filter(line => line.contains(DataNeeded))
x1.take(10).foreach(println)
x1.saveAsTextFile("/home/hdu/workspace/SparkApps/TestOut1")

val spark = SparkSession.builder.master("local").appName("Spark_SQL_basic_example").getOrCreate()
val df = spark.read.format("csv").option("inferSchema","true").load(outputPath + "/" + "part-00000")
println("fileinfo data in dataframe")
df.show(10)

sc.stop()
}