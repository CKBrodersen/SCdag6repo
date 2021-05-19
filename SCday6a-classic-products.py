# Exercise with the classicmodels database
# Created April 2020 by JENR
# Modified May 2021 to reflect changes in beautifultable 1.0.1
# Used in KEA BE-IT 2nd semester SC, day 6

# Show a nice message
print(80*'-')
print('Hello - let\'s connect to classicmodels')

import ClassicConnect as thisDatabase
from beautifultable import BeautifulTable

# Nice function to display result in a table
def prettyprint(result, th, context):
    table = BeautifulTable()
    table.columns.header = th
    table.set_style(BeautifulTable.STYLE_RST)
    for row in result:
        table.rows.append(row)
    print(80*'-')
    print(context)
    print(table)
    print(len(result), 'row(s) returned')

# Connect
thisConn = thisDatabase.dbconnect()

# Define the query - just paste from Workbench, since we have been so clever as to use triple-quotes
q = """
SELECT
    productLine,
    productName,
    productScale,
    productVendor,
    buyPrice
FROM
    classicmodels.products
WHERE
    productScale = '1:10'
ORDER BY productLine, productName DESC
"""

th = ['Category','Name','Scale','Salesperson','Price']

myCursor = thisConn.cursor()
myCursor.execute(q)
myRecords = myCursor.fetchall()

# Display results nicely
prettyprint(myRecords, th, 'Table of models in scale 1:10')

# Disconnect
thisConn.close()
