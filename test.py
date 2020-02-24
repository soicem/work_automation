#-*- coding:utf-8 -*-

import pandas as pd

df_src = pd.read_excel(r'해운대구 반송동.xls')
#print(df_src[['소재지', '지번', '접면']].iloc[0])
#print(df_src.iloc[0])

place = df_src[['소재지', '지번', '접면']].iloc[0]['소재지']
place = place.split(" ")
place = place[0] + " " + place[2]
placeNumber = df_src[['소재지', '지번', '접면']].iloc[0]['지번']
fullAddr = place + " " + placeNumber

df_dst = pd.read_excel(r'해운대구.xls')
#print(df_dst['소재지'][0].replace("부산광역시 ", ""))
#print(len(df_src))
d = {}
for j in range(len(df_src) - 1):
        place = df_src[['소재지', '지번', '접면']].iloc[j]['소재지']
        place = place.split(" ")
        place = place[0] + " " + place[2]
        placeNumber = df_src[['소재지', '지번', '접면']].iloc[j]['지번']
        srcAddr = place + " " + placeNumber
        #print(j, srcAddr)
        d[srcAddr] = df_src[['소재지', '지번', '접면']].iloc[j]['접면']

result = []

for i in range(len(df_dst) - 1):
    dstAddr = df_dst['소재지'][i].replace("부산광역시 ", "")
    if dstAddr in d.keys():
        print(i, d[dstAddr])
        result.append(d[dstAddr])
    else:
        print("-------------------")
        break

df = pd.DataFrame({'Data': result}) 
df.to_excel(r'export_dataframe.xls')
        

        
        
