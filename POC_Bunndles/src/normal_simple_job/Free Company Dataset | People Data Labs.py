# Databricks notebook source
# MAGIC %md
# MAGIC #Free Company Dataset | People Data Labs
# MAGIC
# MAGIC - This is our free company dataset of company profiles with reduced fields. The data in this file is updated quarterly. We also list our paid company dataset.
# MAGIC - This data covers global companies with at least 1 employee in the People Data Labs dataset.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC TESting best palce to edit

# COMMAND ----------

# MAGIC %md
# MAGIC ## Show all tables available in this share.

# COMMAND ----------

# DBTITLE 1,Show all tables in schema
df_tables = spark.sql("SHOW TABLES IN people_data_labs_free_company_dataset.freedatasets")
display(df_tables.select("tableName"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE people_data_labs_free_company_dataset.freedatasets.freecompanydataset;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT industry,count(*) FROM people_data_labs_free_company_dataset.freedatasets.freecompanydataset
# MAGIC GROUP by industry

# COMMAND ----------

# MAGIC %md
# MAGIC ## Example Queries

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE bronze_all_compianies
# MAGIC USING DELTA AS
# MAGIC SELECT * FROM people_data_labs_free_company_dataset.freedatasets.freecompanydataset
# MAGIC

# COMMAND ----------

# DBTITLE 1,Lead list generation
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE silver_fs_us_companies
# MAGIC USING DELTA AS
# MAGIC SELECT * FROM people_data_labs_free_company_dataset.freedatasets.freecompanydataset
# MAGIC WHERE industry='financial services'
# MAGIC AND country='united states';

# COMMAND ----------

# DBTITLE 1,American Airlines // Aviation Companies
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE product_fs_us_companies_analysis
# MAGIC USING DELTA AS
# MAGIC SELECT name, website, founded, size FROM people_data_labs_free_company_dataset.freedatasets.freecompanydataset
# MAGIC WHERE industry='airlines/aviation'
# MAGIC AND country='united states'
# MAGIC AND founded is not null
# MAGIC AND size = '10001+' 
# MAGIC ORDER BY founded DESC;
