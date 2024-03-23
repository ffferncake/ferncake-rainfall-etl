import psycopg2  # import the Postgres library

import pandas as pd

from connection import *

CREATE_STATEMENT = '''CREATE TABLE IF NOT EXISTS rainfall_2021_08_cast \
    (ID SERIAL NOT NULL,\
    강우량계코드 TEXT NOT NULL,\
    강우량계명 TEXT,\
    구청코드 TEXT, \
    구청명 TEXT, \
    우량_10분 NUMERIC, \
    자료수집시각 TEXT);
'''
INSERT_STATEMENT = 'INSERT INTO rainfall_2021_08_cast (강우량계코드,강우량계명,구청코드,구청명,우량_10분,자료수집시각) VALUES (%s,%s,%s,%s,%s,%s)'


df = pd.read_csv('서울시_강우량_정보_2021년08월_utf8.csv',
                 encoding='utf8').replace(",", "")
# df0 = df0.to_string()
# print(df0.head())

rainfall_meter_code = df[df.columns[0]]
rainfall_meter_name = df[df.columns[1]]
district_code = df[df.columns[2]]
district_name = df[df.columns[3]]
rainfall_10mins = df[df.columns[4]]
timestamps = df[df.columns[5]]

# yymm = df0.iloc[:, 0].values
# cccode = df0.iloc[:, 1].values
# ccdesc = df0.iloc[:, 2].values
# rcodecode = df0.iloc[:, 3].values
# rcodedesc = df0.iloc[:, 4].values
# ccaattcode = df0.iloc[:, 5].values
# ccaattdesc = df0.iloc[:, 6].values
# ccaattmmcode = df0.iloc[:, 7].values
# ccaattmmdesc = df0.iloc[:, 8].values

combined_data = tuple(zip(rainfall_meter_code,
                          rainfall_meter_name,
                          district_code,
                          district_name,
                          rainfall_10mins,
                          timestamps))

# print(combined_data)

for i, d in enumerate(combined_data):
    print(i, ' --> ', d)

# def func(x): return float(x[1:].replace(',', ''))

# # # ''' Calling Cleaning Functions & checking'''
# # cleaned_mobile_prices = cleaning(func, price_data)
# # cleaned_mobile_rating = cleaning(float, ratings_data)

data = list(zip(rainfall_meter_code,
                rainfall_meter_name,
                district_code,
                district_name,
                rainfall_10mins,
                timestamps))
# print(data)
conn = database_connect('termproject', 'postgres', 'fernkus42')
database_operation(conn, CREATE_STATEMENT)
database_operation(conn, INSERT_STATEMENT, data)
