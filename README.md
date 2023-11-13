## PySpark Data Processing & Pipelines with Databricks

Microsoft Learning | Data Engineering with Azure

In this mini-project we've bundled up a couple of exercises:

1) Data Processing with Spark
When dealing with large datasets, Spark can significantly improve the time spent on running our queries by distributing the workload among several workers

2) Data Pipeline with Databricks
Databricks offers a very user friendly platform to handle data manipulations, visualizations and dashboards. Additionally, it offers cicd practices allowing one to automate and even schedule your workflows

Below are a few examples of what I've been able to get done using PySpark and Databricks:

![Dashboard](https://github.com/nogibjj/databricks_JCB/assets/33461065/b4da3e4a-f003-437f-9dc5-d907f7f2dc39)
This is a dashboard that I've created using some very simple queries. Here are some screenshots of the Databricks UI and some of the code I used to build these visualizations:

In a Databricks notebook, run the following code to download and import my stock_prices.csv
`mkdir /dbfs/FileStore/shared_uploads/jc1010@duke.edu/stocks`
`wget -O /dbfs/FileStore/shared_uploads/jc1010@duke.edu/stocks/stock_prices.csv https://raw.githubusercontent.com/nogibjj/databricks_JCB/main/stock_prices.csv`

In the following cell, you can load the data into a pyspark dataframe using:
`df = spark.read.load("/FileStore/shared_uploads/stocks/stock_prices.csv", format = "csv", header=True)`

Next, you can create a Delta Table. Delta Tables are very useful as they have version control. 
![delta_table](https://github.com/nogibjj/databricks_JCB/assets/33461065/ab50d5d5-9823-4e83-81df-de175b021ccd)

Databricks notebooks also allow us to use SQL for querying our databases and tables:
![image](https://github.com/nogibjj/databricks_JCB/assets/33461065/1c925f45-2f25-44e4-a7f8-44f9ac92b737)

Using the combined power of Jobs and Schedules, one can automate these visualizations and even send the dashboards to other users. 
![workflow](https://github.com/nogibjj/databricks_JCB/assets/33461065/9a540d3e-c662-4ba9-bac1-a0a39f63f7d5)

So far my project offers data extraction, transformation and loading. Over the coming weeks I shall delve deeper into automation and even integrate some Machine Learning to the data. Hopefully it will provide some useful insights into what SPY is going to be doing in the future!
