# Introduction
<p align="justify"> 
This repistory contains the files and reports for Course Recommendation System created as part of DAEN 690 Capstone project,George Mason University,Spring 2023 under the guidance of <a href="MAILTO:igang@gmu.edu">Dr.Isaac Gang</a></p>

# Background
<p align="justify"> 
Our work introduces numerous machine learning techniques and methods to evaluate and develop a personalized course recommendation system for an existing user. These recommendations are made based on the course popularity that are reported through dashboard visualizations. After the completion of the course, these details are added to the system after successful completion of the courses and the process repeats indefinitely. A recommendation system is a type of information filtering system that predicts the preferences that a user would give to a product or service. In recent years, these systems have grown in popularity because they can help the users save time and make better decisions. One such recommendation system is the course recommendation system. A course recommendation system can provide personalized recommendations for courses to students based on their preferences or areas of interest. These systems produce accurate and relevant courses that match a student's learning goals using various algorithms and techniques. Several key components of the course recommendation system are data gathering, data analysis, and recommendation algorithms. Collecting student data is the first stage in developing a course recommendation system. This data is then analyzed using machine learning algorithms to identify patterns and trends between users and the respective courses that can be used to forecast the course that a student might want to take next. Our results show a high level of prediction accuracy in recommending courses.
</p>

# Getting Started

We recommend [conda](https://docs.conda.io/projects/conda/en/latest/glossary.html?highlight=environment#conda-environment) for environment management, and [VS Code](https://code.visualstudio.com/) for development. To run the [main.py](https://github.com/jaswanth333/daen690_course_recommendation_system/blob/main/main.py) follow the instructions below.


```bash

# 1. Create and activate a new conda environment
conda create -n <environment_name> python=3.10
conda activate <environment_name>

# 2. Install the surprise package
conda install -c conda-forge scikit-surprise

# 3. create a Jupyter kernel
python -m ipykernel install --user --name <environment_name> --display-name <kernel_name>

# 4. Clone this repo within vscode or using command:
git clone https://github.com/jaswanth333/daen690_course_recommendation_system

# 6. Within VS Code:
#   a. Open a notebook, e.g.,notebooks/Preprocessing and EDA.ipynb;  
#   b. Select Jupyter kernel <kernel_name>;
#   c. Run the notebook.

```
# Algorithms
<p align="justify"> 
To evaluate the model performance of distanced based learning algorithms and Matrix factorization alsogirthms we did 5 fold cross validation on the data to obtain (RMSE) Root Mean Square Error and calcuated the training and test time. In addition to that we have calculated the relavant recommendations being provided in the top 5 recommendations of cross validated test data using Mean Average Precision @ k and Mean Average Recall @ k.  

The following table represents the scores achieved on Distance based Learning algorithm i.e. KNN as well as the Matrix Factorization Algorithms such as SVD,SVDpp and NMF.


| Model         | Test RMSE | Train Time | Test Time |     Mean Average Precision @ k    |     Mean Average Recall @ k    |
|---------------|-----------|------------|-----------|:---------------------------------:|:------------------------------:|
| SVD           | 0.932     | 0.058      | 0.013     |                 0.7               |               0.82             |
| SVDpp         | 0.938     | 0.080      | 0.030     |                 0.7               |               0.82             |
| KNNBasic      | 0.982     | 0.582      | 0.437     |                0.67               |               0.87             |
| KNNWithMeans  | 1.117     | 0.567      | 0.452     |                0.63               |               0.93             |
| KNNWithZScore | 1.126     | 0.669      | 0.468     |                 0.7               |               0.82             |
| NMF           | 1.191     | 0.231      | 0.012     |                0.69               |               0.81             |
</p>

# Results
<p align="justify"> 
After evaluating the model accuracy, build time, test time,precision and recall it can be concluded that the Baseline Matrix factorization model SVD is performing better .This model is capable of handling missing values  and noise in the data and data sparsity problems. Finally, with the SVD algorithm in place an user interactive function with preprocessing pipeline and test set creation pipeline has been implemented. 
</p>

# Future Work
<p align="justify"> 
In Future Work, Course recommendation systems could benefit from incorporating additional data sources. Information such as the description of the course, domain of the course and the reviews can play an important role in providing recommended courses pertaining to the domain and ignore the ones with negative feedback. 
On the additional is in place, the existing model can be updated by implementing deep learning models or hybrid models that combine multiple techniques could be used to improve the accuracy of recommendations and learn the complex relationships between items and users.
Also, more knowledge on the social and contextual elements that influence course selection could potentially enhance course recommendation systems.
Overall, there are many areas of future work for course recommendation systems. By incorporating more data sources, machine learning techniques, and social/contextual information, and by improving the explain ability of recommendations and considering long-term outcomes, these systems could become even more valuable tools for students and educators alike.
</p>
