import mysql.connector
conn = mysql.connector.connect(
    host="localhost", username="root", password="root")
mycursor = conn.cursor()

