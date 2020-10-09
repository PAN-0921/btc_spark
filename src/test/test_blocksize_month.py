import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'src')

from package.load_csv_from import *
from package.blocksize_month import *



df=load_csv_from(file_path="data/btc.csv")
df1 = df.withColumn("NEW_DATE", df['date'].substr(1, 7))
# df1.show()

# print("total record count: %d" % (df.count()))

df2=blocksize_month(df1).show()