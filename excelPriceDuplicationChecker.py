#-*- coding:utf-8 -*-

import pandas as pd

nameOfSrc = "20200226_26140_개별주택_조사목록(부산 서구) 다수동 시청제출(1)"
df_src = pd.read_excel(nameOfSrc + ".xls")
#print(df_src[["지번", "동구분", "20년 토지단가"]].iloc[0])
#print(len(df_src))
#df = pd.DataFrame({'Data': result}) 
#df.to_excel(nameOfSrc + "_접면" + ".xls")
print(df_src[["읍면동", "지번", "동구분", "20년 토지단가"]].iloc[0]["지번"])
duplication = {}

for i in range(0, len(df_src)):
    current = df_src[["읍면동", "지번", "동구분", "20년 토지단가"]].iloc[i]
    place = current["읍면동"]
    number = current["지번"]
    price = current["20년 토지단가"]
    keyOfCurrent = place + " " + number
    if keyOfCurrent not in duplication.keys():
        duplication[keyOfCurrent] = price
    else:
        if duplication[keyOfCurrent] != price:
            duplication[keyOfCurrent] = -1;

from xlwt import Workbook
import xlwt
book = Workbook(style_compression=2)
sheet1 = book.add_sheet('Sheet 1')
    
for i in range(0, len(df_src)):
    current = df_src[["읍면동", "지번", "동구분", "20년 토지단가"]].iloc[i]
    place = current["읍면동"]
    number = current["지번"]
    seperator = current["동구분"]
    price = current["20년 토지단가"]
    keyOfCurrent = place + " " + number
    st = xlwt.easyxf('pattern: pattern solid;')
    if duplication[keyOfCurrent] == -1:
        st.pattern.pattern_fore_colour = 80
    else:
        st.pattern.pattern_fore_colour = 100
    #sheet1.write(i, 0, place, st)
    sheet1.write(i, 0, number, st)
    sheet1.write(i, 2, price, st)
    sheet1.write(i, 4, price, st)
    
book.save('simple.xls')






