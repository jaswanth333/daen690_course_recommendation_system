import pandas as pd
import numpy as np

def preprocess(df):
    df.columns = [c.replace(' ', '_') for c in df.columns]
    df.columns = df.columns.str.lower()
    df = df.rename(columns={'demographic_data': 'gender','course_selected': 'course_name'})
    df['course_name']=df['course_name'].str.replace('Gulf News - ','')
    df['course_name']=df['course_name'].str.replace('Bootcamp - ','')
    #df['course_name']=df['course_name'].str.replace('`- Python/JAVA/HTML/C/C++`','')
    df['course_name']=df['course_name'].str.replace(' Winter Internship Program','')
    df['course_name']=df['course_name'].str.replace(' - Microsoft Arcade','')
    df['course_name']=df['course_name'].str.replace(' - Block-Based','')
    #df['course_name']=df['course_name'].str.replace(' - Block-Based','')
    df['course_name']=df['course_name'].str.replace('Robotics/Virtual Robotics/Robotics Programming','Robotics')
    df['course_name']=df['course_name'].str.split('(').str[0]
    df['course_name']=df['course_name'].str.split('-').str[0]

    for i in df.columns:
        if df[i].dtype=='object':
            df[i]=df[i].map(str.strip)
        else:
            pass    
    #print("Preprocessed Courses")

    replacers = {
    'Python Coding': 'Python Programming',
    #'Game and App Development': 'Game Development',
    #'Graphic Designing & Animation':'Graphic Designing',
    'Public Speaking & Entrepreneurship':'Public Speaking ',
    #'Artificial Intelligence for Non Programmers':'Artificial Intelligence',
    'Space STEM':'Robotics',
    #'VEX Robotics':'Virtual Robotics',
    #'FIRST LEGO LEAGUE ':'LEGO Robotics',
    #'Scratch Coding':'Programming',
    #'Game Development with Unity':'Game Development',
    #'Young Game Developer':'Game Developement',
    'School':'Robotics',
    #'Artificial Intelligence & Machine Learning':'Artificial Intelligence and Machine Learning',
    #'Virtual Robotics & Mechatronics':'Virtual Robotics',
    'Artificial Intelligence Summer Program & Internship':'Artifical Intelligence',
    'Programming & Coding ':'Programming',
    'FIRST Lego League ':'LEGO Robotics',
    #'Game Combat Championship ' :'Game Developement',
    'JAVA':'JAVA Programming',
    'World Robot Olympiad Webinar':'Robotics',
    'STEM Sr':'Robotics',
    #'Microsoft Arcade':'Game Developement',
    #'Augmented & Virtual Reality' :'Virtual Reality',
    #'App Design and Development':'App Development',
    'Public Speaking, Design Thinking and Junior Entrepreneur Program for Students':'Young Entrepreneur',
    'Mid Term Program':'Artifical Intelligence',
    'Winter Camp 2022':'Robotics',
    'Summer Camp 2022':'Robotics',
    'Winter Camp 2021':'Robotics',
    'Coding for kids':'Coding For kids',
    'Summer Camps':'Robotics',
    'Python':'Python Programming',
    'Artifical Intelligence':'Artificial Intelligence',
    'Artificial Intelligence Program':'Artificial Intelligence',
    'Artificial Intelligence & Machine Learning':'Artificial Intelligence and Machine Learning',
    'ALIF Robotics Workshop':'Robotics',
    'Tech Summer Camp for Juniors' :'Robotics',
    'AI' :'Artificial Intelligence',
    #'Drone Technology & Aerodynamics':'Drone Technology',
    #'Coding for kids':'Programming',
    'Game Dev with SCRATCH':'Game Development',
    'Canon Junior Photography':'Photography',
    #'Coding For Kids':'Programming',
    'VEX Robotics Competition ':'Virtual Robotics',
    'VEX IQ Competition ': 'Virtual Robotics',
    'FIRST LEGO LEAGUE':'First LEGO League',
    'Metaverse':'Virtual Reality',
    'STEM Jr':'Robotics',
    #'3D Designing':'Graphic Designing',
    #'3D Designing and Printing':'Graphic Designing',
    'Graphics Designing':'Graphic Designing',
    'Spring Camps':'Robotics',
    'CIS Stem Junior Year':'Robotics',
    'CIS Tech Innovator Year':'Robotics',
    'Robotics Regent':'Robotics',
    'Game Development Microsoft Arcade':'Microsoft Arcade',
    'Game Development Block':'Game Development'
    }

    df['course_name'] = df['course_name'].replace(replacers)

    df = df.loc[~((
    (df['course_name']=='Art & Craft for Juniors')|
    (df['course_name']=='Technology Onsite ')|
    (df['course_name']=='French Language Course')|
    (df['course_name']=='Speech and Drama')|
    #(df['course_name']=='Young Product Designer')|
    (df['course_name']=='Tech Innovator')|
    (df['course_name']=='Train the Trainer')|
    (df['course_name']=='CIS, Dubai')|
    #(df['course_name']=='Young Honcho')|
    (df['course_name']=='Half Term Camp 2022')|
    (df['course_name']=='Technology Boot Camp')|
    (df['course_name']=='World Robot Olympiad ')|
    (df['course_name']=='Photography')|
    (df['course_name']=='Public Speaking')|
    (df['course_name']=='Spring Camp')|
    (df['course_name']=='Arduino')))]

    #print("Preprocessed Age")
    ##preprocess age
    df = df[(df.age != "14-Oct") & (df.age != "9-May")]
    df['age'] = df['age'].replace(['1'], 'Year 1')
    df['age'] = df['age'].replace(['2'], 'Year 2')
    df['age'] = df['age'].replace(['3'], 'Year 3')
    df['age'] = df['age'].replace(['4'], 'Year 4')
    df['age'] = df['age'].replace(['5'], 'Year 5')
    df['age'] = df['age'].replace(['6'], 'Year 6')
    df['age'] = df['age'].replace(['7'], 'Year 7')
    df['age'] = df['age'].replace(['8'], 'Year 8')
    df['age'] = df['age'].replace(['9'], 'Year 9')
    df['age'] = df['age'].replace(['10'], 'Year 10')
    df['age'] = df['age'].replace(['11'], 'Year 11')
    df['age'] = df['age'].replace(['12'], 'Year 12')
    df['age'] = df['age'].replace(['13'], 'Year 13')
    df['age'] = df['age'].replace(['14'], 'Year 14')
    df['age'] = df['age'].replace(['15'], 'Year 15')
    df['age'] = df['age'].replace(['Year 1'], '5')
    df['age'] = df['age'].replace(['Year 2'], '6')
    df['age'] = df['age'].replace(['Year 3'], '7')
    df['age'] = df['age'].replace(['Year 4'], '8')
    df['age'] = df['age'].replace(['Year 5'], '9')
    df['age'] = df['age'].replace(['Year 6'], '10')
    df['age'] = df['age'].replace(['Year 7'], '11')
    df['age'] = df['age'].replace(['Year 8'], '12')
    df['age'] = df['age'].replace(['Year 9'], '13')
    df['age'] = df['age'].replace(['Year 10'], '14')
    df['age'] = df['age'].replace(['Year 11'], '15')
    df['age'] = df['age'].replace(['Year 12'], '16')
    df['age'] = df['age'].replace(['Year 13'], '17')
    df['age'] = df['age'].replace(['Year 14'], '18')
    df['age'] = df['age'].replace(['Year 15'], '19')
    df['age'] = df['age'].replace(['FS 1'], '5')
    df['age'] = df['age'].replace(['FS 2'], '6')
    df['age'] = df['age'].replace(['KG 1'], '5')
    df['age'] = df['age'].replace(['KG 2'], '6')
    df['age'] = df['age'].replace(['KG2'], '6')
    df['age'] = df['age'].replace(['University/College'], '16')
    df['age'] = df['age'].replace(['Working Professional'], '16')

    df=df.groupby("age").filter(lambda x: len(x) > 5)
    ## Typecasting
    df['age'] = pd.to_numeric(df['age'])

    ##Caterogrizing
    df['gender'] = df['gender'].astype('category')
    df['modes_of_learning'] = df['modes_of_learning'].astype('category')
    df['session'] = df['session'].astype('category')
    df['difficulty_level'] = df['difficulty_level'].astype('category')
    df['field_of_interest'] = df['field_of_interest'].astype('category')
    ##new col
    col         = 'age'
    conditions  = [ (df[col] >=5) & (df[col]<10), (df[col] >=10) & (df[col]<14),(df[col] >=14)]
    choices     = ['Elementary school (5-9)', 'Middle school (10-13)','High school/College (14+)']

    df["education"] = np.select(conditions, choices, default=np.nan)
    #create stu id
    np.random.seed(42)
    df['student_id'] = np.random.randint(1, 4000, df.shape[0])
    #creare course id     
    course_df=pd.DataFrame(df['course_name'].unique(),columns=["course_name"])
    index = pd.Index(range(0, len(course_df.index), 1))
    course_df["course_id"] = course_df.index
    df=df.merge(course_df,on="course_name",how="left")
    #result df
    final_df=df[['student_id','student_name','age','nationality',
       'education','school','field_of_interest','course_id',
       'course_name','session','course_rating','difficulty_level','modes_of_learning']]
    print("-------------------------Data preprocessed---------------------------")
    return final_df