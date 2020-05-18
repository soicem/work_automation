import pandas as pd
import numpy as np

import glob
all_data = pd.DataFrame()
data = pd.ExcelFile("부산 시가수준.xlsx")
names = ["해운대구", "수영구", "남구", "부산진구", "동구", "서구", "중구", "연제구", "양산시"]
#names = ["해운대구"]



for name in names:
    df = pd.read_excel(data, sheet_name=name)
    prev = ""
    my_list = []
    for line in range(len(df)):
        target = str(df.iloc[line][1])
        if target[len(target) - 1] == "가" or target[len(target) - 1] == "동":
            prev = target
        my_list.append(prev)
        
            
        #print(df.iloc[line][1])
    with open(name + ".txt", 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)
        
#df = df.drop([0, 1]).drop([len(df) - 1, len(df)-1])
#all_data = all_data.append(df, ignore_index=True)
#all_data.to_excel("진주" + ".xls")


