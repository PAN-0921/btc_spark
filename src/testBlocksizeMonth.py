import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.getcwd()+'/lib')

from loadCSVfrom import *
from blocksizeMonth import *



df=loadCSVfrom(file_path="data/btc.csv")
df1 = df.withColumn("NEW_DATE", df['date'].substr(1, 7))
df1.show()

print("total record count: %d" % (df.count()))

df2=blocksizeMonth(df1)
df2.filter("NEW_DATE LIKE '2018%' OR NEW_DATE LIKE '2019%'").show()