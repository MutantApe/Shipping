import numpy as np
import MySQLdb

#import YangMIng_Daily_Noon

from datetime import datetime as dt
import pandas as pd
from datetime import datetime as dt
import mysql.connector
from sqlalchemy import create_engine
import xlrd

df = pd.read_excel('/home/muitant/Documents/04oct2018to16apr2019.xlsx', header=[0])

# data = df.loc[3:df.shape[0] - 2]
# print(data)
noon_time_column_data = df['Unnamed: 7'].iloc[3:df.shape[0] - 2]

last_noon_time=df['Unnamed: 7'].iloc[-3]
print('last noon time in df',last_noon_time)

dt= noon_time_column_data[197]
if dt==last_noon_time:
    print('same date',dt)

pdt = df.index[df['Unnamed: 7'] == dt].astype(int)[0]
# print(pdt)
# book = xlrd.open_workbook('/home/muitant/Documents/04oct2018to16apr2019.xlsx')
# sheet = book.sheet_by_index(0)
# #
# # # shipnames=sheet.r
# # # print(sheet.values)
# row_list=sheet.row_values(rowx=4,start_colx=0,end_colx=sheet.ncols)
# print(tuple(row_list))
# #


# df = pd.read_excel('/home/muitant/Documents/04oct2018to16apr2019.xlsx',header=None)
# data_in_df=df.iloc[1:df.shape[1]]
# # # ls_d=data_in_df.to_dict()
# print(tuple(data_in_df))
#
# #


#
# for i in range(0 , df.shape[0]-1):
#         first = data_in_df.loc[i]
#         print(first)

# data = df.iloc[3:df.shape[0]-2]
#
# l = data['Unnamed: 7']
# ls = list(l)
# print(ls)
# m = []
# for i in ls:
#    m.append(i.timestamp())
#
# print(m[-1])

# engine = create_engine('mysql+pymysql://fm:password@localhost:3306/mydb', echo=False)
# cnx = engine.raw_connection()
# data = pd.read_sql('SELECT * FROM yang_ming_daily_noon', cnx)
# data.to_sql(name= df, con=cnx, if_exists = 'append', index=False)


# SQL work



# engine = create_engine('mysql://fm:password@localhost:3306/mydb')
# #
# # #cursor= engine.cursor()
# dft= pd.read_sql_table('yang_ming_daily_noon', con=engine)
# cols=dft.columns[1:-1]
# # print(tuple(dft.iloc[-1:]))
# #print(tuple(cols))
# # #
# field_names = tuple(cols)
# field_values= tuple(row_list)
# #
# with engine.connect() as con:
# #
#     rs = con.execute('INSERT INTO yang_ming_daily_noon (' + ','.join(field_names) + ') VALUES (' + ','.join('?' * len(field_names)) + ')' , field_values)
columns_list=[
        '',
        '',
        ''
]