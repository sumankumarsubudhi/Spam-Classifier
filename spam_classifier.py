import pandas as pd
from sklearn.model_selection import train_test_split

# Importing the dataset into a pandas dataframe
df = pd.read_table('SMSSpamCollection', sep = '\t', header = None, names = ['labels','sms_message']
               
# Converting our labels to binary variables for ease of computation
df['label'] = df.label.map({'ham':0, 'spam':1})

