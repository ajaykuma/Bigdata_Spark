package main.scala
import org.apache.spark.SparkContext 
import org.apache.spark.SparkContext._ 
import org.apache.spark.SparkConf 

object MThirteenthApp extends App {
  
    print("hello")
    val conf = new SparkConf().setAppName("AccumExample").setMaster("local")
    //val conf = new SparkConf().setAppName("HelloSpark0127")
    val sc = new SparkContext(conf)
    val accum = sc.longAccumulator("SumAccumulator")
    //sc.parallelize(Array(1, 2, 3)).foreach(x => accum.add(x))
    sc.parallelize(1 to 10000).foreach(x => accum.add(x))
    println(accum.value)
    //sc.stop()
  }
