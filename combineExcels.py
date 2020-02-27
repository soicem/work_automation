import pandas as pd
import numpy as np

import glob
print(glob.glob("*.xls"))
all_data = pd.DataFrame()
dt = ""
for f in glob.glob("*.xls"):
    df = pd.read_excel(f)
    df = df.drop([0, 1]).drop([len(df) - 1, len(df)-1])
    all_data = all_data.append(df, ignore_index=True)
all_data.to_excel("진주" + ".xls")
