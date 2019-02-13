import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbp_test"
)


#print(mydb)

mycursore = mydb.cursor()

# Create database command
#mycursore.execute("CREATE DATABASE dbp_test")

'''
# show databases
mycursore.execute("SHOW DATABASES")
for db in mycursore:
    print(db)
'''

# insert into table
sql_query = "INSERT INTO students(name, age) VALUES(%s, %s)"

'''

student1 = ("sanat", 22)
student2 = ("ajoy", 20)
mycursore.execute(sql_query, student1)
mycursore.execute(sql_query, student2)

'''

'''
# insert multiple data at the same time
students = [
    ("Sanat Mondal", 25),
    ("Ajoy Kumar Paul", 20),
    ("Nazmul Haque", 23),
    ("Ronju Ahmed", 22),
]

mycursore.executemany(sql_query, students)
mydb.commit()
'''


'''

# Read the data

mycursore.execute("select * from students")
myresult = mycursore.fetchall()
for row in myresult:
    print(row)
'''

# mycursore.execute("select * from students where age > 22 and name like '%Sanat%'")
sql_q = "select * from students where name like 'sanat%'"
mycursore.execute(sql_q, "Mon")
myresult = mycursore.fetchall()
for row in myresult:
    print(row)


'''
mycursore.execute("select age from students")
myresult = mycursore.fetchone()
for row in myresult:
    print(row)
'''

