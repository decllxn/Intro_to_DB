#!/usr/bin/env python3
# Author - Declan Munene
# Date - 27/7/2024
# Description - python scripts that creates an sql database

import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect (
            host="localhost",
            user="decllxn",
            password="King Declan1234",
            database="alx_book_store"
     )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    for x in mycursor:
        print(x)

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Failed to connect to database: {e}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")
