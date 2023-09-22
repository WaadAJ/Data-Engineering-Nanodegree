import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket (customer landing zone)
S3bucketcustomerlandingzone_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-lakehous/customer/landing/"],
        "recurse": True,
    },
    transformation_ctx="S3bucketcustomerlandingzone_node1",
)

# Script generated for node Privacy Filter
PrivacyFilter_node1693695408482 = Filter.apply(
    frame=S3bucketcustomerlandingzone_node1,
    f=lambda row: (not (row["shareWithResearchAsOfDate"] == 0)),
    transformation_ctx="PrivacyFilter_node1693695408482",
)

# Script generated for node Trusted customer zone
Trustedcustomerzone_node3 = glueContext.write_dynamic_frame.from_options(
    frame=PrivacyFilter_node1693695408482,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-lakehous/customer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="Trustedcustomerzone_node3",
)

job.commit()
