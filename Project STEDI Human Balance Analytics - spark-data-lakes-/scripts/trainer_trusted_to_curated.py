import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1693706166917 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_trusted",
    transformation_ctx="AmazonS3_node1693706166917",
)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="step_trainer_trusted",
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Join
Join_node1693706198813 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AmazonS3_node1693706166917,
    keys1=["sensorreadingtime"],
    keys2=["timestamp"],
    transformation_ctx="Join_node1693706198813",
)

# Script generated for node Drop Fields
DropFields_node1693706290718 = DropFields.apply(
    frame=Join_node1693706198813,
    paths=["user"],
    transformation_ctx="DropFields_node1693706290718",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1693706290718,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-lakehous/step_trainer/curated/",
        "compression": "snappy",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
