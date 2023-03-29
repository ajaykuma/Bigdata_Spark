#This is a Maven based project
--After downloading scala-ide, create a new project
File > new > Scala Project > SparkAppsSB

#Running Appl from IDE
To be able to compile code within IDE (taken care by Maven) and run apps directly, make sure 'Build path' for project is configured.
Right click on project > Build path > Configure Build path 
--set scala compiler to use 'project settings' & choose 'Latest 2.11'
--Check if points to your Java (say 1.8)

--convert your project into Maven project
--This should have created pom.xml file
--update pom.xml as provided in project with dependencies
--click and expan on Maven dependencies to check spark based dependencies

Now all code should compile fine.

--Run any application (say AfirstApp.scala)

#packaging your applications
right click on project and run as > Maven install
--check if it shows 'Build Success' <refresh project>
--check in target folder for packaged jar

--to run using spark-submit use this JAR
--from command line
C:\Users\Ajay kumar\workspace\SparkAppsSB>spark-submit.cmd --master local --class main.scala.AfirstApp target\\SparkAppsSB-0.0.1-SNAPSHOT.jar

