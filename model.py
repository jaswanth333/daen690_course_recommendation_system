import pandas as pd
import numpy as np
import pickle
from surprise import Dataset,Reader,SVD,accuracy
from surprise.model_selection import cross_validate
from test import test_set
from recommendations import recommendations


def svd_model(preprocessed_df,student_id):
    reader = Reader(rating_scale=(1,5))
    #Create Course ID's
    course_df=pd.DataFrame(preprocessed_df['course_name'].unique(),columns=["course_name"])
    index = pd.Index(range(0, len(course_df.index), 1))
    course_df["course_id"] = course_df.index
    
    validation_set,enrolled=test_set(preprocessed_df,student_id,course_df)
    data = Dataset.load_from_df(preprocessed_df[['student_id', 'course_id', 'course_rating']], reader)
    trainSet = data.build_full_trainset()
    print("------------------------------------------------------------------")
    model_input = input("1:Update Model | 2.Run pre-trained model\n")
    if model_input=='1':
        np.random.seed(1)
        print("---------------------------Training the model----------------------------")
        svd_algo = SVD(n_factors=150,n_epochs=5,lr_all=0.005,reg_all=0.1)
        cross_validate(svd_algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
        pickle.dump(svd_algo, open('svd_algo.sav', 'wb'))
        predictions = svd_algo.test(validation_set)
        print("------------------------------Model Trained------------------------------")
        recommendations(course_df,predictions,enrolled)
        
    else:
        print("------------------------Running pre-trained model-------------------------")
        svd_algo = pickle.load(open('svd_algo.sav', 'rb'))
        cross_validate(svd_algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
        predictions = svd_algo.test(validation_set)
        #pass to predict function
        recommendations(course_df,predictions,enrolled)
