import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# Importing the dataset into a pandas dataframe
df = pd.read_table('SMSSpamCollection', sep = '\t', header = None, names = ['labels','sms_message']
               
# Converting the labels to binary variables for ease of computation
df['label'] = df.label.map({'ham':0, 'spam':1})

# Splitting the dataset into a training and testing set by using the train_test_split method in sklearn                   
X_train, X_test, y_train, y_test = train_test_split(df['sms_message'], df['label'])
                   
# Instantiating the CountVectorizer method
count_vector = CountVectorizer()

# Fitting the training data and then return the matrix
training_data = count_vector.fit_transform(X_train)

# Transforming testing data and return the matrix
testing_data = count_vector.transform(X_test)                   
