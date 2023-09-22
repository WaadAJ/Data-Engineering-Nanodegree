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

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-lakehous/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node Amazon S3
AmazonS3_node1693705359104 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_curated",
    transformation_ctx="AmazonS3_node1693705359104",
)

# Script generated for node Join
Join_node1693705324415 = Join.apply(
    frame1=S3bucket_node1,
    frame2=AmazonS3_node1693705359104,
    keys1=["serialNumber"],
    keys2=["serialnumber"],
    transformation_ctx="Join_node1693705324415",
)

# Script generated for node Drop Fields
DropFields_node1693705451889 = DropFields.apply(
    frame=Join_node1693705324415,
    paths=[
        "customername",
        "email",
        "phone",
        "birthday",
        "serialnumber",
        "registrationdate",
        "lastupdatedate",
        "sharewithresearchasofdate",
        "sharewithpublicasofdate",
        "sharewithfriendsasofdate",
    ],
    transformation_ctx="DropFields_node1693705451889",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1693705451889,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-lakehous/step_trainer/trsuted/",
        "compression": "snappy",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
