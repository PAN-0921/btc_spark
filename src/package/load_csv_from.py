from package.spark_session import *

def load_csv_from(file_path:str):
	df=spark_session.read.csv(file_path,header=True,sep=",")
	return df
