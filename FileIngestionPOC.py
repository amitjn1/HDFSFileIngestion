import sys
from pyspark.sql import SQLContext 
from pyspark import SparkConf, SparkContext 

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print >> sys.stderr, "Usage: FileIngestionPOC.py <file location>"
		exit(-1)

	fileloc = sys.argv[1]

	spark_conf = SparkConf().setMaster('local').setAppName('test') 
	sc = SparkContext(conf=spark_conf) 

	sqlContext = SQLContext(sc) 

	from pyspark.sql import functions as F
	from pyspark.sql.types import *   
# create custom schema as per the file to be ingested
	customSchema = StructType([                                                                                      
		StructField("RowID", IntegerType()),
		StructField("Item_Desc", StringType()),
		StructField("FullName", StringType()),
		StructField("Field4", StringType()),
		StructField("Field5", StringType()),
		StructField("Field6", StringType()),
		StructField("Field7", StringType()),
		StructField("Field8", StringType()),
		StructField("Field9", StringType()),
		StructField("Field10", StringType())
	])

# load csv files using the custom schema with spark-csv library from databricks

	df = sqlContext.read.format("com.databricks.spark.csv").option("header", "false").load("file:" + fileloc, schema=customSchema)

# Mask the FullName field to replace the actual values with X's

	df = df.withColumn('FullName', F.regexp_replace(df.FullName,'.*$', 'X'))

	df.write.format('com.databricks.spark.csv').save('/pocdir/sampledata1')

	sc.stop()
