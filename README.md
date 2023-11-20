## Individual Project #3: Databricks ETL (Extract Transform Load) Pipeline

Building upon the previous [mini-projects](https://github.com/nogibjj/databricks_JCB), I have integrated data ingestion from YahooFinance using the yfinance project. Additionally, I've scheduled an entire ETL pipeline to run weekly so I can end each week with a brief description of what my favorite stocks have been doing.

### Data Ingestion

This project makes use of the Databricks Lakehouse. It takes the best of Data Warehouses and Data Lakes to provide a single platform for all data workloads. One of the great advantages is the use of Delta Lakes. Delta is an open-source data storage file format that provides ACID transactions, unified batchand streaming, schema evolution, table history AND time-travel.

This is particularly useful for this project. Weekly I download data from the following stocks: stock_tickers = ['EEM', 'IWM', 'SPY', 'XBI', 'XLC', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP', 'XLRE', 'XLU', 'XLV', 'XLY', 'XOP', 'XRT'] and update a DeltaTable object.
