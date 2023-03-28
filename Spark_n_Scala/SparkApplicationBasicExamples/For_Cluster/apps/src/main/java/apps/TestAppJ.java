package apps;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;

import scala.Tuple2;
import java.util.Arrays;

public class TestAppJ {

	private static void wordCount(String fileName)
	{
		SparkConf sparkConf = new SparkConf().setMaster("local").setAppName("TestApp");
		JavaSparkContext sparkContext = new JavaSparkContext(sparkConf);
		JavaRDD<String> inputFile = sparkContext.textFile(fileName);
		JavaRDD<String> wordsFromFile = inputFile.flatMap(content -> Arrays.asList(content.split(" ")).iterator());
		JavaPairRDD countData = wordsFromFile.mapToPair(t -> new Tuple2(t,1)).reduceByKey((x,y) -> (int)x + (int) y);
		System.out.println(countData.collect());
		countData.saveAsTextFile("output");
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
