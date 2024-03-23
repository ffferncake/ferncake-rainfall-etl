import requests
from bs4 import BeautifulSoup as bs
import psycopg2 as pg
import pandas as pd

#### only for web scraping
# def check_n_response(url, parser='html.parser'):
#     # TODO Add functionality for generating response
#     page = requests.get(url)

#     if page.status_code in range(200, 300):
#         print('Request was successful')
#         return bs(page.text, parser)
#     else:
#         # print(f'Request was denied the error code is {page.status_code}')
#         print('yayyyyyyyy')


# def generate_html(soup_obj):
#     # TODO Add functionality gor generating html
#     with open('temp.html', 'w+', encoding='utf-8') as fp:
#         fp.write(soup_obj.prettify())


# def extraction(soup_object, tag, _class, attr, index=None, single=False):
#     # TODO generate iterable of different lengths with clean text
#     data = [i.get_text() for i in soup_object.find_all(tag, {_class: attr})]
#     if single:
#         return data[0]
#     elif index:
#         return data[:index]
#     return data


# def cleaning(format, iterable):
#     # TODO apply list(map())
#     return list(map(format, iterable))


def database_connect(name, user, password):
    # TODO return an open connection
    try:
        db_connection = pg.connect(host="localhost",
                                   database="scsi",
                                   user="postgres",
                                   password="fernkus42",
                                   port='5432')
        print('That connection was successful')
        return db_connection
    except pg.DatabaseError as e:
        # print(f'error happened {e}')
        print('error')


def database_operation(connection, statement, data=None):
    # TODO execute statement and commit to database and close the connection
    try:
        cursor = connection.cursor()
        if data:
            for d in data:
                cursor.execute(statement, d)
                print(d)
        else:
            cursor.execute(statement)
        connection.commit()
        print('The transaction was successful')
    except pg.DatabaseError as e:
        print(f'error happened {e}')
        # print('error')


def close_connection(connection, statement, data=None):
    if connection:
        # cursor.close()
        connection.close()
        print('Connection was closed successfully')
