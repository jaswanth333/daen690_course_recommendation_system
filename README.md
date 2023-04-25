# Introduction
This repistory contains the files and reports for Course Recommendation System created as part of DAEN 690 Capstone project

# Getting Started
We recommend [conda](https://docs.conda.io/projects/conda/en/latest/glossary.html?highlight=environment#conda-environment) for environment management, and [VS Code](https://code.visualstudio.com/) for development. To install the recommenders package and run an example notebook on Linux/WSL:


```bash

# 2. Create and activate a new conda environment
conda create -n <environment_name> python=3.10
conda activate <environment_name>

# 3. Install the recommenders package with examples
conda install -c conda-forge scikit-surprise

# 4. create a Jupyter kernel
python -m ipykernel install --user --name <environment_name> --display-name <kernel_name>

# 5. Clone this repo within vscode or using command:
git clone https://github.com/microsoft/recommenders.git

# 6. Within VS Code:
#   a. Open a notebook, e.g., examples/00_quick_start/sar_movielens.ipynb;  
#   b. Select Jupyter kernel <kernel_name>;
#   c. Run the notebook.

```
# Algorithms

| Model         | Test RMSE | Train Time | Test Time |
|---------------|-----------|------------|-----------|
| SVD           | 0.932     | 0.058      | 0.013     |
| SVDpp         | 0.938     | 0.080      | 0.030     |
| KNNBasic      | 0.982     | 0.582      | 0.437     |
| KNNWithMeans  | 1.117     | 0.567      | 0.452     |
| KNNWithZScore | 1.126     | 0.669      | 0.468     |
| NMF           | 1.191     | 0.231      | 0.012     |

# Results
After evaluating the model accuracy, build time and test time it can be concluded that SVD is performing better .This model is capable of handling missing values  and noise in the data and data sparsity problems. Finally, with the SVD algorithm in place an user interactive function with preprocessing pipeline and test set creation pipeline has been implemented. 

To view the running model run model.py (daen690_course_recommendation_system/blob/main/model.py)
