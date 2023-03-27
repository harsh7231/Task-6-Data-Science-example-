import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
df = pd.read_csv('customer_data.csv')
X = df.drop('purchase', axis=1)
y = df['purchase']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
y_pred = lr_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion matrix:\n', conf_matrix)
new_data = np.array([[25, 'Male', 1000], [35, 'Female', 5000]])
new_df = pd.DataFrame(new_data, columns=['age', 'gender', 'income'])
new_df['gender'] = new_df['gender'].apply(lambda x: 1 if x == 'Male' else 0)
new_pred = lr_model.predict(new_df)
print('Predictions:', new_pred)
