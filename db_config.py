import mysql.connector

def get_database_connection():
     connection = mysql.connector.connect(
         host = 'gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com',
         user = '31fACzuAR5V1pxE.root',
         password = '9YK1AgrtrcEfU7Bk',
         database = 'student_task_manager',
         port = 4000
     )

     return connection