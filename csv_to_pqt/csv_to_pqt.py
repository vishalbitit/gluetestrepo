import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

csv_df = spark.read.csv("s3://vishaldevbucket/inbound/csv-data/sales-data/")
csv_df.write.mode('overwrite').parquet("s3://vishaldevbucket/outbound/csvoutput/")

job.commit()