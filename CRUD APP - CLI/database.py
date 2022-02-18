# Memakai library mysql connector
import mysql.connector

# Melakukan akses database dengan data sebagai berikut
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'crud-python',
)