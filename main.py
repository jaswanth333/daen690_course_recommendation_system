import pandas as pd
import numpy as np
from surprise import Dataset,accuracy
from preprocess import preprocess
from sqlconnection import data
from model import svd_model

#df=pd.read_csv("dataset/student_course_data.csv")
def couse_recommendation():
    n = 100
    while n > 0:
     n -= 1
     student_id = None
     while student_id is None:
            try:
                student_id = int(input("Enter student id: "))
                print("-----------------------------------------------------------------------")
                df=data()
                processed_data=preprocess(df)
                processed_data.to_csv("dataset/processed_data.csv",index=False)
            except ValueError:
                print("Student record not found in DB!")
            finally:
                if student_id in processed_data['student_id'].values:
                    svd_model(processed_data,student_id)
                    pass
                else:
                    print("Enter Correct Student id Again")
                    #validation_set = None
                    student_id = None
couse_recommendation()