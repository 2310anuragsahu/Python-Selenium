import cx_Oracle
import os
os.environ['PATH'] = "Path of the Oracle Instant Client"


connection = cx_Oracle.connect("username", "password", "<oracle server/IP address> / <service id/name>")

cursor = connection.cursor()

cursor.execute("Some query")

cursor.close()
connection.commit()
connection.close()
