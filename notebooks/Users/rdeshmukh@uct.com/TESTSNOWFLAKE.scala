// Databricks notebook source
import org.apache.spark.sql._

// Use secrets DBUtil to get Snowflake credentials.


// COMMAND ----------

import org.apache.spark.sql._

// COMMAND ----------


 
val options = Map(
  "sfUrl" -> "ULTRA_CLEAN_HOLDINGS_DATAPLATFORM.snowflakecomputing.com",
  "sfUser" -> "RDESHMUKH",
  "sfPassword" -> "Uct123$567",
  "sfDatabase" -> "UCT_DEVELOPMENT",
  "sfSchema" -> "LANDING",
  "sfWarehouse" -> "COMPUTE_WH",

)

// COMMAND ----------

spark.sparkContext.setLogLevel("DEBUG")

// COMMAND ----------

// Generate a simple dataset containing five values and write the dataset to Snowflake.
spark.range(5).write
  .format("snowflake")
  .options(options)
  .option("dbtable", "table_name11")
  .save()

// COMMAND ----------

// MAGIC %python
// MAGIC base_url = "ULTRA_CLEAN_HOLDINGS_DATAPLATFORM.snowflakecomputing.com"
// MAGIC 
// MAGIC import socket
// MAGIC HOST = socket.gethostbyname(base_url)
// MAGIC PORT = 443
// MAGIC with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
// MAGIC     s.connect((HOST, PORT))

// COMMAND ----------

// MAGIC %sh
// MAGIC curl -v http://oscp.sca1b.amazontrust.com

// COMMAND ----------

// MAGIC %sh nc -vz 192.168.168.31 7077

// COMMAND ----------

// MAGIC %sh nc -vz 192.168.168.44 41877

// COMMAND ----------

// MAGIC % curl -u username:password https://YOUR_INSTANCE_NAME.cloud.databricks.com/api/1.2/clusters/list
// MAGIC 
// MAGIC [
// MAGIC   {
// MAGIC       "driverIp": "10.0.236.4",
// MAGIC       "id": "batVenom",
// MAGIC       "jdbcPort": 10000,
// MAGIC       "name": "Mini-Cluster",
// MAGIC       "numWorkers": 2,
// MAGIC       "status": "Running"
// MAGIC   }
// MAGIC ]

// COMMAND ----------

// MAGIC %fs ls /mnt/uct-landing-gen-dev/