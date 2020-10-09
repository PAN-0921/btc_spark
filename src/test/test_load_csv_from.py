import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)

sys.path.insert(1, 'src')

from package.load_csv_from import *

df=load_csv_from(file_path=os.getcwd()+"/data/btc.csv")
df.show();