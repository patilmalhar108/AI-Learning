import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('Churn_Modelling.csv')
df.head()
df.info()
df.describe()
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])
print(df)
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis = 1)
print(df.shape)
y = df.pop('Exited')
x = df
print(x.shape)
print(y.shape)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
print(x_train)