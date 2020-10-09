from pyspark.sql import DataFrame
from pyspark.sql import functions as func

def aggregate_blocks(df:DataFrame):
	df.agg(func.sum("blockCount")).show()