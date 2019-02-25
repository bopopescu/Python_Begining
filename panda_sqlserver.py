import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=172.16.1.131\SQL2014;"
                      "Database=PythonLearning;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM tblLocation')

for row in cursor:
    print('row = %r' % (row,))
    print("\n")

