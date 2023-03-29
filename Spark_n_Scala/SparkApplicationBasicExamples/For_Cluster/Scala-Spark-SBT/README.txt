#This is a SBT based project

#Running Appl from IDE
To be able to compile code within IDE and run apps directly, make sure 'Build path' for project is configured.
Right click on project > Build path > Configure Build path 
--set scala compiler to use 'project settings' & choose 'Latest 2.11'
--Check if points to your Java (say 1.8), if not set it right.
--In Java Build path > Libraries > Add external jars > select all jars from your spark folder/jars/
Now all code should compile fine.

Now we can run application from within IDE

#To package and run applications
--setup SBT on your machine and then go into the workspace to package applications
C:\Users\<username>\workspace\SparkAppsSB>sbt package
---sample output----
[info] Updated file C:\Users\Ajay kumar\workspace\SparkAppsSB\project\build.properties: set sbt.version to 1.8.2
[info] welcome to sbt 1.8.2 (Oracle Corporation Java 1.8.0_341)
[info] loading project definition from C:\Users\Ajay kumar\workspace\SparkAppsSB\project
[info] loading settings for project sparkappssb from build.sbt ...
[info] set current project to Simple Project (in build file:/C:/Users/Ajay%20kumar/workspace/SparkAppsSB/)
[info] compiling 15 Scala sources to C:\Users\Ajay kumar\workspace\SparkAppsSB\target\scala-2.11\classes ...
[warn] multiple main classes detected: run 'show discoveredMainClasses' to see the list
[success] Total time: 15 s, completed Mar 29, 2023 2:34:03 PM
---sample output ends----
Refresh project and check in target folder
Directory of C:\Users\Ajay kumar\workspace\SparkAppsSB\target\scala-2.11
it should show
simple-project_2.11-1.1.0.jar

#to test it
from command line (assuming spark is setup either with YARN or without YARN i.e. local mode & if spark path is set in environment variables)
--From project folder (as appl may be pointing to files in project folder)
C:\Users\Ajay kumar\workspace\SparkAppsSB>spark-submit.cmd --master local 
--class main.scala.AfirstApp target\\scala-2.11\\simple-project_2.11-1.1.0.jar

--check if output folder was created within your project





