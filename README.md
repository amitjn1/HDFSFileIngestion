# HDFSFileIngestion
POC to copy files to HDFS file system folder in Hadoop using PySpark

Environment 
-	Hadoop sandbox from Hortonworks or Cloudera 

Programming language
-	Pyspark 
- Spark version 1.6.0

Usecase
-	Copy data from local filesystem in linux to HDFS file system folder in Hadoop
-	Files will be in CSV format
-	Mask data in one of the column in files, e.g. replace the value of that column with ‘XXXX’

Solution
-	Write a program in Pyspark which should be executed from command line on Hadoop sandbox with parameter(s) that specifies the directory path and file name wild cards and another parameter that specifies the field number that should be masked.
For example:
/home/data/samplefiles/SampleCSVFile*.csv 3
Here, 3 specifies that 3rd field should be masked
Nice to have:
If we can specify the list of fields to be masked. For example, to mask 3rd, 5th and 7th field
/home/data/samplefiles/SampleCSVFile*.csv [3,5,7]

-	Program should read all files from the directory that match the file name wild cards.
-	While processing the data pyspark program should replace the content of one the fields to XXXX for data masking. This should be 3rd field in the sample CSV file attached below.
-	Copy modified data to a HDFS directory
-	Rename the processed files in the local folder with an extension .bak and move to another folder named ‘/dirname_processed/’.
