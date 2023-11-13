from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# create spark session
spark = SparkSession.builder.config("spark.driver.host", "localhost").getOrCreate()

# spark = SparkSession.builder \
#     .appName("StockPrices") \
#     .master("local[*]") \
#     .getOrCreate()


def read_data(path="stock_prices.csv"):
    """
    Read the data from the path specified.
    """
    try:
        df = spark.read.format("csv").option("header", "true").load(path)
    except FileNotFoundError:
        pass
    df = df.withColumn("Datetime", F.to_timestamp("Datetime", "dd/MM/yyyy HH:mm"))
    return df


def create_database():
    """
    Create database and table in spark.
    """
    spark.sql("CREATE DATABASE IF NOT EXISTS stock_prices")
    spark.sql("USE stock_prices")
    spark.sql("DROP TABLE IF EXISTS raw_prices")
    # spark.sql(
    #     "CREATE TABLE raw_prices (Datetime DATE, Instrument STRING, Price_type STRING, Price FLOAT)"
    # )
    spark.sql(
        """
    CREATE TABLE IF NOT EXISTS raw_prices (
        Datetime DATE, 
        Instrument STRING, 
        Price_type STRING, 
        Price FLOAT
    ) USING parquet
    """
    )
    pass


def insert_data(df, table_name):
    """
    Insert data into table.
    """
    df.write.mode("overwrite").insertInto(table_name)
    pass


def create_ohlc(instrument):
    """
    Create OHLC table for a given instrument.
    """
    # Use the stock_prices database
    spark.sql("USE stock_prices")

    # Load the raw_prices table
    raw_prices = spark.table("raw_prices")

    # Filter for instrument
    instrument_prices = raw_prices.filter(raw_prices.Instrument == instrument)

    # Create the new DataFrame
    spy = (
        instrument_prices.groupBy("Datetime", "Instrument")
        .agg(
            F.max(
                F.when(instrument_prices.Price_type == "Open", instrument_prices.Price)
            ).alias("Open"),
            F.max(
                F.when(instrument_prices.Price_type == "High", instrument_prices.Price)
            ).alias("High"),
            F.max(
                F.when(instrument_prices.Price_type == "Low", instrument_prices.Price)
            ).alias("Low"),
            F.max(
                F.when(instrument_prices.Price_type == "Close", instrument_prices.Price)
            ).alias("Close"),
        )
        .orderBy(F.desc("Datetime"))
    )

    # Save the DataFrame as a table
    spy.write.saveAsTable(instrument, mode="overwrite")
    pass


def get_max_min(instrument):
    """
    Query the OHLC table for a given instrument to get the max and min price.
    If table does not exist, create it.
    """
    # Use the stock_prices database
    spark.sql("USE stock_prices")

    # Check if table exists
    if instrument not in spark.catalog.listTables("stock_prices"):
        create_ohlc(instrument)

    # Load the table
    ohlc = spark.table(instrument)

    # return a dataframe with max_price and min_price as columns,
    # and the max_date and min_date values as rows
    max_close = ohlc.agg(F.max("Close").alias("max_price")).collect()[0][0]
    min_close = ohlc.agg(F.min("Close").alias("min_price")).collect()[0][0]
    max_close_date = ohlc.filter(ohlc.Close == max_close).collect()[0][0]
    min_close_date = ohlc.filter(ohlc.Close == min_close).collect()[0][0]

    # return dataframe with max and min price and date
    return spark.createDataFrame(
        [(max_close, max_close_date), (min_close, min_close_date)], ["price", "date"]
    )
