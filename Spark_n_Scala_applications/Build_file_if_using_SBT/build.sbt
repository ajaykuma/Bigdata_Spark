name := "Simple Project"
version := "1.1.2"
scalaVersion := "2.11.8"
val sparkVersion = "2.4.3"


resolvers ++= Seq(
    "apache-snapshots" at "https://repository.apache.org/snapshots/"
)


libraryDependencies ++= Seq(

"org.apache.spark" %% "spark-core" % sparkVersion,

"org.apache.spark" %% "spark-sql" % sparkVersion,

"org.apache.spark" %% "spark-mllib" % sparkVersion,

"org.apache.spark" %% "spark-streaming" % sparkVersion,

"org.apache.spark" %% "spark-hive" % sparkVersion
)
