#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd


# In[27]:


data = pd.read_csv('internship_train.csv')


# In[28]:


data


# In[29]:


data.describe()


# In[30]:


from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split


# In[31]:


modelLR = LinearRegression()
modelNN = MLPRegressor()
modelRF = RandomForestRegressor()


# In[32]:


data.head()


# In[33]:


x = data.iloc[:, 0:53]
y = data.iloc[:, 53:54]


# In[34]:


y


# In[35]:


Xtrain, Xtest, Ytrain, Ytest = train_test_split(x,y, test_size = 0.2, random_state = 1)


# In[36]:


Xtest


# In[37]:


Ytest


# In[38]:


modelLR.fit(Xtrain,Ytrain)
modelNN.fit(Xtrain,Ytrain)
modelRF.fit(Xtrain,Ytrain)


# In[46]:


print(modelLR.score(Xtest,Ytest))
print(modelNN.score(Xtest,Ytest))
print(modelRF.score(Xtest,Ytest))


# In[47]:


from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


# In[48]:


LRpred = modelLR.predict(Xtest)
NNpred = modelNN.predict(Xtest)
RFpred = modelRF.predict(Xtest)


# In[49]:


print(mean_squared_error(LRpred,Ytest))
print(mean_squared_error(NNpred,Ytest))
print(mean_squared_error(RFpred,Ytest))


# In[50]:


## Second model


# In[95]:


data2 = pd.read_csv('internship_hidden_test.csv')


# In[ ]:





# In[96]:


import joblib


# In[97]:


x_train = data2


# In[98]:


modelLR.predict(x_train)


# In[99]:


pred = modelLR.predict(x_train)


# In[71]:


print(pred)


# In[105]:


##


# In[100]:


####


# In[102]:


data2['target'] = pred


# In[103]:


data2


# In[108]:


data2.to_csv('done.csv')


# In[152]:


####


# In[1]:


pip freeze > requirements.txt


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




