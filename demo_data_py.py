# -*- coding: utf-8 -*-
"""demo_data.py

Please see colab notebook with printed statements at: https://colab.research.google.com/drive/1kh58_WrfRmFatKUZFpa7AT_Vpk3a5hGP
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_demo_data = '''
CREATE TABLE demo_table (
    s CHAR(1),
    x NUMERIC,
    y NUMERIC
)
'''

curs.execute(create_demo_data)

insert = """INSERT INTO demo_table 
VALUES ('g', 3, 9),
('v', 5, 7),
('f', 8, 7);"""

curs.execute(insert)

rows = curs.execute('SELECT COUNT(*) FROM demo_table;').fetchone()
print('The number of rows is:', rows[0])

greater_than_5 = curs.execute('SELECT COUNT(*) FROM demo_table WHERE x >=5 AND y >= 5;').fetchone()
print('The number of rows where x and y each exceed 5 is: ', greater_than_5[0])

y_unique = curs.execute('SELECT COUNT(DISTINCT y) FROM demo_table;').fetchone()
print('The number of unique values of y is: ', y_unique[0])
