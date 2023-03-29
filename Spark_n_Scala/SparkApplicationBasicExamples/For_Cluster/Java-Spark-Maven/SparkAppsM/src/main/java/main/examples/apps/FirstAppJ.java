package main.examples.apps;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;
import java.util.Arrays;

public class FirstAppJ {

	private static void wordCount(String fileName)
	{
		SparkConf sparkConf = new SparkConf().setMaster("local").setAppName("TestApp");
		JavaSparkContext sparkContext = new JavaSparkContext(sparkConf);
		JavaRDD<String> inputFile = sparkContext.textFile(fileName);
		JavaPairRDD<String, Integer> counts = inputFile.flatMap(s -> Arrays.asList(s.split(" ")).iterator())
			    .mapToPair(word -> new Tuple2<>(word, 1))
			    .reduceByKey((a, b) -> a + b);
		//System.out.println(counts.collect());
		counts.saveAsTextFile("output");
		sparkContext.close();
		
	}
	
	public static void main(String[] args)
	{
		if (args.length == 0) {
			System.out.println("Please enter a source file");
			System.exit(0);
		}
		wordCount(args[0]);
		
	}
}
