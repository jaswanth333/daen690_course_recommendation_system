import pandas as pd
from surprise import accuracy
# from itertools import chain


def recommendations(course_df,predictions,enrolled):
    #print("Validation RMSE:",accuracy.rmse(predictions))
    #print("Validation MAE:",accuracy.mae(predictions))
    pred = pd.DataFrame(predictions)
    pred['err'] = abs(pred.est - pred.r_ui)
    n  = int(input("Enter no: of Recommendations:"))
    best_predictions = pred.sort_values(by='err')['iid'].head(n).to_list()
    courses=course_df.loc[course_df['course_id'].isin(best_predictions)]["course_name"].to_list()
    # courses = list(chain(*courses))
    # enrolled = list(chain(*enrolled))
    print("------------------------------Courses Enrolled--------------------------------\n",enrolled)
    print("-------------------------------Recommendations------------------------------\n",courses)
