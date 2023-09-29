#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 1. Load the data
df = pd.read_csv('bmi.csv')

# 2. Pre-process Data (One-Hot Encoding for BmiClass)
df = pd.get_dummies(df, columns=["BmiClass"], drop_first=True)

# Setting up features and target variable
X = df.drop("Weight", axis=1)
y = df["Weight"]

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# 5. Test the Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")


# In[8]:


pip install pandas matplotlib seaborn


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bmi.csv')


# In[10]:


plt.figure(figsize=(10,6))
sns.histplot(df['Bmi'], kde=True)
plt.title('Distribution of BMI')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()


# In[11]:


plt.figure(figsize=(10,6))
sns.scatterplot(x=df['Age'], y=df['Bmi'])
plt.title('Age vs. BMI')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.show()


# In[12]:


plt.figure(figsize=(10,6))
sns.regplot(x=df['Height'], y=df['Weight'])
plt.title('Height vs. Weight')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()


# In[13]:


plt.figure(figsize=(10,6))
sns.countplot(x=df['BmiClass'], order=df['BmiClass'].value_counts().index)
plt.title('Distribution across BMI Classes')
plt.xlabel('BMI Class')
plt.ylabel('Count')
plt.show()


# In[14]:


# age groups
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

plt.figure(figsize=(10,6))
sns.barplot(x=df['AgeGroup'], y=df['Bmi'])
plt.title('Average BMI across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Average BMI')
plt.show()


# In[15]:


plt.figure(figsize=(10,6))
sns.boxplot(x=df['Bmi'])
plt.title('Box plot of BMI')
plt.show()


# In[16]:


plt.figure(figsize=(10,6))
sns.violinplot(x=df['AgeGroup'], y=df['Weight'])
plt.title('Weight distribution across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Weight')
plt.show()


# In[ ]:




