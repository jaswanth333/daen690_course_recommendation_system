from surprise import Reader
from surprise import Dataset

def test_set(preprocessed_df,student_id,course_df):    
    validation_set = []
    reader = Reader(rating_scale=(1,5))
    data = Dataset.load_from_df(preprocessed_df[['student_id', 'course_id', 'course_rating']], reader)
    trainSet = data.build_full_trainset()
    inner_uid = trainSet.to_inner_uid(student_id)
    targetUser = inner_uid #inner_id of the target user
    user_item_ratings = trainSet.ur[targetUser]
    fillValue = trainSet.global_mean
    user_item_ratings = trainSet.ur[inner_uid]
    user_items = [item for (item,_) in (user_item_ratings)]
    ratings = trainSet.all_ratings()
    for iid in trainSet.all_items():
        if(iid not in user_items):
            validation_set.append((trainSet.to_raw_uid(targetUser),
                                      trainSet.to_raw_iid(iid),
                                      fillValue))
    print("Student",student_id,"has" ,len(validation_set),"unenrolled courses")
    
    enrolled=course_df.loc[course_df['course_id'].isin(user_items)]['course_name'].to_list()
    return validation_set,enrolled