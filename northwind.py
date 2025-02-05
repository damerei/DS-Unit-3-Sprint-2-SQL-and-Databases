# -*- coding: utf-8 -*-
"""Please see colab link with printed statements for grading at: 

    https://colab.research.google.com/drive/1QwZ9gXbF_uXUIl3lthRC9kXNoUg11XDQ
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('northwind_small.sqlite3')

curs=conn.cursor()

top_10 = curs.execute("""SELECT ProductName, UnitPrice 
FROM Product 
ORDER BY UnitPrice DESC LIMIT 10;
""").fetchall()

print('The ten most expensive items are: ', top_10)

average_age = curs.execute('SELECT AVG(HireDate - BirthDate) FROM Employee').fetchall()
print('The average age of employees at the time of hiring is: ', average_age)

city_variance = curs.execute('SELECT City, HireDate, AVG(HireDate - BirthDate) FROM Employee GROUP BY City').fetchall()
print('Average age of employees at hiring, in different cities: ', city_variance)

top_10_with_supplier = """SELECT Product.ProductName, Supplier.CompanyName 
         FROM Product, Supplier 
         WHERE Product.SupplierId = Supplier.Id \
         ORDER BY UnitPrice DESC LIMIT 10;"""

result_top_10_with_supplier = curs.execute(top_10_with_supplier).fetchall()

print('The top ten most expensive items, listed along with their suppliers, are: ', result_top_10_with_supplier)

largest_unique_category = """
SELECT Category.CategoryName FROM Category
  WHERE Category.Id = 
    (SELECT CategoryID FROM
      (SELECT Count(*) as prod_count, Product.CategoryId
      FROM Product GROUP BY Product.CategoryId
      ORDER BY prod_count DESC LIMIT 1));"""

result_largest_unique_category = curs.execute(largest_unique_category).fetchall()

print('The largest category by number of unqiue products is: ', result_largest_unique_category)

