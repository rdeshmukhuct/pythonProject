# Databricks notebook source
aws_bucket_name = "uct-landing-fin-qa"
mount_name = "uct-landing-fin-qa"
dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s" % mount_name)
display(dbutils.fs.ls("/mnt/%s" % mount_name))

# COMMAND ----------

aws_bucket_name = "uct-archive-gen-dev"
mount_name = "uct-archive-gen-dev"
dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s" % mount_name)
display(dbutils.fs.ls("/mnt/%s" % mount_name))

# COMMAND ----------

# MAGIC %fs ls /mnt/uct-landing-gen-dev/SAP/

# COMMAND ----------

# MAGIC %fs ls /mnt/uct-transform-gen-dev/SAP

# COMMAND ----------

# MAGIC %fs ls /mnt/uct-consumption-gen-dev/tmp/

# COMMAND ----------

# MAGIC %fs ls /mnt/uct-archive-gen-dev

# COMMAND ----------

aws_bucket_name = "uct-consumption-gen-dev"
mount_name = "uct-consumption-gen-dev"
dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s" % mount_name)
display(dbutils.fs.ls("/mnt/%s" % mount_name))

# COMMAND ----------

aws_bucket_name = "uct-transform-gen-dev"
mount_name = "uct-transform-gen-dev"
dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s" % mount_name)
display(dbutils.fs.ls("/mnt/%s" % mount_name))

# COMMAND ----------

aws_bucket_name = "uct-landing-gen-dev"
mount_name = "uct-landing-gen-dev2"
dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s" % mount_name)
display(dbutils.fs.ls("/mnt/%s" % mount_name))

# COMMAND ----------

dbutils.fs.ls("/mnt/")

# COMMAND ----------


dbutils.fs.unmount("/mnt/uct-landing-gen-dev6")


# COMMAND ----------

display(dbutils.fs.ls("/mnt/uct-landing-gen-dev4/SAP/MARA/"))

# COMMAND ----------

# Define the input format and path.
read_format = 'delta'
load_path = '/databricks-datasets/learning-spark-v2/people/people-10m.delta'
 
# Load the data from its source.
people = spark.read \
  .format(read_format) \
  .load(load_path)
 
# Show the results.
display(people)

# COMMAND ----------

# Define the output format, output mode, columns to partition by, and the output path.
write_format = 'delta'
write_mode = 'overwrite'
partition_by = 'gender'
save_path = '/mnt/uct-consumption-gen-dev/tmp/delta/people-10m'
 
# Write the data to its target.
people.write \
  .format(write_format) \
  .partitionBy(partition_by) \
  .mode(write_mode) \
  .save(save_path)

# COMMAND ----------

import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.DataFrame