# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "sanjayrampura01@gmail.com",
	password = "Blaackword01@"
)

# Printing the connection object
print(mydb)
import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "sanjayrampura01@gmail.com",
	password = "Blaackword01@",
	database = "geeksforgeeks"
)d

cursor = mydb.cursor()

# Creating a table called 'gfg' in the
# 'geeksforgeeks' database
cursor.execute("CREATE TABLE gfg (name VARCHAR(255), user_name VARCHAR(255))")
