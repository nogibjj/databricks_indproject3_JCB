## Individual Project #3: Databricks ETL (Extract Transform Load) Pipeline

Building upon the previous [mini-projects](https://github.com/nogibjj/databricks_JCB), I have integrated data ingestion from YahooFinance using the yfinance project. Additionally, I've scheduled an entire ETL pipeline to run weekly so I can end each week with a brief description of what my favorite stocks have been doing.

### Data Ingestion

This project makes use of the Databricks Lakehouse. It takes the best of Data Warehouses and Data Lakes to provide a single platform for all data workloads. One of the great advantages is the use of Delta Lakes. Delta is an open-source data storage file format that provides ACID transactions, unified batchand streaming, schema evolution, table history AND time-travel.

This is particularly useful for this project. Weekly I download data from the following stocks: stock_tickers = ['EEM', 'IWM', 'SPY', 'XBI', 'XLC', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP', 'XLRE', 'XLU', 'XLV', 'XLY', 'XOP', 'XRT'] and update a DeltaTable object. Each time I do so, a new version of the table is created. This allows me to query the table as it was at any point in time. 

![deltatable](https://github.com/nogibjj/databricks_indproject3_JCB/assets/33461065/a38c0e9b-0e32-4ca3-b143-6eeeaec39f4b)
![merge new](https://github.com/nogibjj/databricks_indproject3_JCB/assets/33461065/359d7b10-a3a5-4236-b589-6cd3d4d5df08)

### Data Transformation

With the raw data updated, I wish to create an OHLC (Open, High, Low, Close) table specifically for SPY.

![spy](https://github.com/nogibjj/databricks_indproject3_JCB/assets/33461065/abc5e792-52e2-4c56-a64c-0d5cd5785d0e)

### Data Load

I can now query the spy table to see how the stock has been performing. 

![latest spy](https://github.com/nogibjj/databricks_indproject3_JCB/assets/33461065/7b4d8781-a9d7-4acc-83f3-df8c919fab89)

### Dashboard

I also created a dashboard that provides a visual representation of SPY's performance relative to EEM.

![dashboard](https://github.com/nogibjj/databricks_indproject3_JCB/assets/33461065/de40a0af-7f2a-4a54-ad3c-cbfe8675ce8d)

### Scheduling the ETL Pipeline

Finally, I scheduled the entire ETL pipeline to run weekly on Fridays at 5pm. This allows me to end each week with a brief description of what my favorite stocks have been doing.

![schedule](https://github.com/nogibjj/databricks_indproject3_JCB/assets/33461065/e0ce1820-c336-4acd-b486-8f0884a99536)

![email screenshot](https://github.com/nogibjj/databricks_indproject3_JCB/assets/33461065/9b4b7d83-9637-4895-b6d9-951e5ef447bb)
