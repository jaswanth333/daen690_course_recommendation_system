import mysql.connector as connection
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
def data():
    try:
        mydb = connection.connect(host="localhost", database = 'student_course_data',user="root", passwd="J4swanth",use_pure=True)
        query = "Select * from sc_data;"
        df = pd.read_sql(query,mydb)
        mydb.close() #close the connection
    except Exception as e:
        mydb.close()
        print(str(e))
    return df       
