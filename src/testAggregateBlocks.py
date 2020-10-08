import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.getcwd()+'/lib')

from loadCSVfrom import *
from aggregateBlocks import *


df=loadCSVfrom(file_path=os.getcwd()+"/data/btc.csv")
print("total record count: %d" % (df.count()))

aggregateBlocks(df)