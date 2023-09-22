# Song Play Analysis with S3 and Redshift -- Data Warehouse Project

## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As a data engineer, I was tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. I'll be able to test my database and ETL pipeline by running queries given by the analytics team from Sparkify and compare my results with their expected results.

### Schema for Song Play Analysis

the database schema was created using the song and event datasets, it follows a star schema, which is a common design pattern for data warehouses. This schema consists of a fact table (songplays) and multiple dimension tables (users, songs, artists, and time). The fact table contains the measures (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent), and the dimension tables contain the descriptive attributes related to each dimension.

The ETL pipeline connects to the Sparkify Redshift database, loads the log_data and song_data into staging tables, and transforms them into the five final tables.

The ETL pipeline starts by copying the data from the S3 bucket into the staging tables (staging_events and staging_songs) using the COPY command. Then, the data is transformed and inserted into the final tables using INSERT statements. The INSERT statements handle duplicate records where appropriate.

## Project Structure

The project includes files as bellow:

-   `create_table.py`  creates fact and dimension tables for the star schema in Redshift.
-   `etl.py`  loads data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
-   `sql_queries.py`  defines you SQL statements, which will be imported into the two other files above.
-   `README.md`  provides discussion on your process and decisions for this ETL pipeline.

## Project Steps

Below are steps to complete each component of this project.

### Create Table Schemas

1.  Design schemas for the fact and dimension tables
2.  Write a SQL  `CREATE`  statement for each of these tables in  `sql_queries.py`
3.  Complete the logic in  `create_tables.py`  to connect to the database and create these tables
4.  Write SQL  `DROP`  statements to drop tables in the beginning of  `create_tables.py`  if the tables already exist. 
5.  Launch a redshift cluster and create an IAM role that has read access to S3.
	- Create a new  `IAM user`  in your AWS account
	-  Give it AdministratorAccess and Attach policies
	-  Use access key and secret key to create clients for  `EC2`,  `S3`,  `IAM`, and  `Redshift`.
	- Create an  `IAM Role`  that makes  `Redshift`  able to access  `S3 bucket`  (ReadOnly)
	-  Create a  `RedShift Cluster`  and get the  `DWH_ENDPOIN(Host address)`  and  `DWH_ROLE_ARN`  and fill the config file.
7.  Add redshift database and IAM role info to  `dwh.cfg`.
8.  Test by running  `create_tables.py`  and checking the table schemas in the redshift database. You can use Query Editor in the AWS Redshift console for this.

### Build ETL Pipeline

1.  Implement the logic in  `etl.py`  to load data from S3 to staging tables on Redshift.
2.  Implement the logic in  `etl.py`  to load data from staging tables to analytics tables on Redshift.
3.  Test by running  `etl.py`  after running  `create_tables.py`  and running the analytic queries on your Redshift database to compare your results with the expected results.
4.  Delete your redshift cluster when finished.

## To Run the Project
1.  Run  `create_tables.py` to create tables.
    
2.  Run  `etl.py` to execute ETL process.