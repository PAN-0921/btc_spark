import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'src')

from package.load_csv_from import *
from package.aggregate_blocks import *


df=load_csv_from(file_path="data/btc.csv")
print("total record count: %d" % (df.count()))

aggregate_blocks(df)