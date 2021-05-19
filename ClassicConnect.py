from mysql import connector
import mysql.connector
from mysql.connector import connection

def dbconnect():
    connection = mysql.connector.connect(
    host="localhost",
    database="classicmodels",
    user="root",
    password="root"
)

    return connection