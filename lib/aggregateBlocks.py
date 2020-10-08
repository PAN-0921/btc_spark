from pyspark.sql import DataFrame
from pyspark.sql import functions as func

def aggregateBlocks(df:DataFrame):
	df.agg(func.sum("blockCount")).show()