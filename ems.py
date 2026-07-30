from os import system
def system(StrOrBytesPath):
    pass

## import mysql.connector
import mysql.connector

## create connection to the database
conn = mysql.connector.connect(
    host="localhost", username="root", password="root", database = "employee")

## create menu function to display menu options
def menu():
    system("cls")
    print("{:>60}".format("*********************************************"))
    print("{:>60}".format("-->> Chalfouh Employee Management System <<--"))
    print("{:>60}".format("*********************************************"))
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit\n")

menu()