package main.scala
import org.apache.spark.SparkContext 
import org.apache.spark.SparkContext._ 
import org.apache.spark.SparkConf 
import org.apache.spark.storage.StorageLevel

object AfirstApp {
  def main(args: Array[String]) {
    print("hello")
    //val conf = new SparkConf().setAppName("HelloSpark0110").setMaster("local")
    val conf = new SparkConf().setAppName("HelloSpark0610")
    val sc = new SparkContext(conf)
    val x = sc.textFile("/mydata/cv000_29416.txt",2)
    val y = x.flatMap(n => n.split(" ")).persist(StorageLevel.MEMORY_ONLY)
        val z = y.map(n => (n,1))
       val result = z.reduceByKey(_+_)
    result.saveAsTextFile("/mydata/outp1")
    result.take(10).foreach(println)
    sc.stop()
  }}
