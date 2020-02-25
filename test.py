#-*- coding:utf-8 -*-

import pandas as pd

nameOfSrc = input("접면이 있는 파일 이름: ")
df_src = pd.read_excel(nameOfSrc + ".xls")

place = df_src[['소재지', '지번', '접면']].iloc[0]['소재지']
place = place.split(" ")
place = place[0] + " " + place[2]
placeNumber = df_src[['소재지', '지번', '접면']].iloc[0]['지번']
fullAddr = place + " " + placeNumber

nameOfDst = input("대상 파일 이름: ")
df_dst = pd.read_excel(nameOfDst + ".xls")
d = {}
for j in range(len(df_src) - 1):
        place = df_src[['소재지', '지번', '접면']].iloc[j]['소재지']
        place = place.split(" ")
        place = place[0] + " " + place[2]
        placeNumber = df_src[['소재지', '지번', '접면']].iloc[j]['지번']
        srcAddr = place + " " + placeNumber
        d[srcAddr] = df_src[['소재지', '지번', '접면']].iloc[j]['접면']

result = []

for i in range(len(df_dst) - 1):
    dstAddr = df_dst['소재지'][i].replace("부산광역시 ", "")
    if dstAddr in d.keys():
        print(dstAddr, d[dstAddr])
        result.append(d[dstAddr])
    else:
        result.append("x")
        print("xxxxxxxxxxxxxxxxxxxx")
df = pd.DataFrame({'Data': result}) 
df.to_excel(nameOfSrc + "_접면" + ".xls")
        

        
        
