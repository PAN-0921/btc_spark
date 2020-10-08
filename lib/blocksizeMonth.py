from pyspark.sql import DataFrame
from pyspark.sql import functions as func

def blocksizeMonth(df:DataFrame):
	res = df.groupBy('NEW_DATE').agg(func.sum("blocksize"))
	res.show()
	return res 