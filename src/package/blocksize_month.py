from pyspark.sql import DataFrame
from pyspark.sql import functions as func

def blocksize_month(df:DataFrame):
	res = df.groupBy('NEW_DATE').agg(func.sum("blocksize")).filter("NEW_DATE LIKE '2018%' OR NEW_DATE LIKE '2019%'")
	return res 