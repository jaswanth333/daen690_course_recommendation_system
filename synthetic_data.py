from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata
from preprocess import preprocess
import pandas as pd
import numpy as np

#Import the data and preprocess it
df=pd.read_csv("dataset/student_course_data.csv")
processed_data=preprocess(df)

#Store the metadata for data generation
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=processed_data)

#Synthetic data model
synthesizer = SingleTablePreset(
    metadata,
    name='FAST_ML'
)

#Training and generation
synthesizer.fit(
    data=processed_data
)
synthetic_data = synthesizer.sample(
    num_rows=50000
)
print("Generating synthetic data...")
#Creating a column with 30000 userID's
synthetic_data['student_id'] = np.random.randint(1,30000, synthetic_data.shape[0])
#Writing the data to CSV
synthetic_data.to_csv("dataset/synthetic_data.csv",index=False)
print("Synthetic Data Generated...")