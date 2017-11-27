# HDFS File Ingestion
POC to copy files to HDFS file system in Hadoop using PySpark

## Technical Design

- Freely available sample CSV files from http://www.sample-videos.com/download-sample-csv.php were used for this POC.
- CSV files were placed into the "/home/pocuser/Downloads/" local folder on the linux sandbox.
- CSV Data Source for Apache Spark 1.x - spark-csv (com.databricks.spark.csv) library was used to correctly load the data. This library takes care of the commas included as part of the text in some of the fields.
- Files does not have header, so a custom schema was applied in the program.
- Program Name: FileIngestionPOC.py
- Usage: `FileIngestionPOC.py [Path to csv files with file masking]`

### Environment 
-	Hadoop sandbox from Hortonworks or Cloudera 

### Programming language
-	Pyspark 
- Spark version 1.6.0

### Usecase
-	Copy data from local filesystem in linux to HDFS file system folder in Hadoop
-	Files will be in CSV format with no header
-	Mask data in one of the column in files, e.g. replace the value of that column with ‘XXXX’

### Solution

MVP - Minimum viable product
-	Write a program in Pyspark which should be executed from command line on Hadoop sandbox with parameter(s) that specifies the directory path on local file system, file name with wild cards.
For example:

[applicationname.py] /home/data/samplefiles/SampleCSVFile*.csv
-	Program should read all files from the directory that match the file name wild cards.
-	While processing the data pyspark program should replace the content of one the fields to XXXX for data masking. This should be FullName field in the sample CSV file attached below.
-	Copy modified data to a HDFS directory

### Future Improvements
- Accept JSON file formats
- Parametrize the list of fields and the fields to be masked
