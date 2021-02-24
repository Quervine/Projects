#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# In[2]:


data = pd.read_csv(r'C:\Users\Quervin Espinal\Desktop\TSLA (2).csv')
#print(data)


# In[3]:


fig = go.Figure([go.Scatter(x=data['Date'], y=data['High'])])

fig.update_layout(
    title={'text': "Tesla Price Chart",
          'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Price')
fig.show()


# In[4]:


data2 = pd.read_excel(r'C:\Users\Quervin Espinal\Desktop\TSLA(2).xlsx')
#print(data2)


# In[5]:


fig1 = px.bar(data2, y = 'EPS', x = 'Date', title = 'TSLA Quarterly EPS')
fig1.show()


# In[11]:


dataN = pd.read_csv(r'C:\Users\Quervin Espinal\Desktop\NIO (1).csv')
dataN2 = pd.read_csv(r'C:\Users\Quervin Espinal\Desktop\NIO (2).csv')


# In[12]:


figA = go.Figure()

figA.add_trace(go.Scatter(x=dataN2['Date'], y=dataN2['High'],
                          mode = 'lines',
                          name = 'NIO'))
               
figA.add_trace(go.Scatter(x=dataT['Date'], y=dataT['High'],
                         mode = 'lines',
                         name = 'TSLA'))

figA.update_layout(
    title={'text': "Tesla VS NIO",
          'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})               
figA.update_xaxes(title_text='Date')
figA.update_yaxes(title_text='Price')

figA.show()


# In[13]:


dataS = pd.read_csv(r'C:\Users\Quervin Espinal\Desktop\SPY (2).csv')
dataT = pd.read_csv(r'C:\Users\Quervin Espinal\Desktop\TSLA (4).csv')


# In[10]:


figB = go.Figure()

figB.add_trace(go.Scatter(x=dataS['Date'], y=dataS['High'],
                          mode = 'lines',
                          name = 'SPY'))
               
figB.add_trace(go.Scatter(x=dataT['Date'], y=dataT['High'],
                         mode = 'lines',
                         name = 'TSLA'))
figB.update_layout(
    title={'text': "Tesla VS SPY",
          'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
               
figB.update_xaxes(title_text='Date')
figB.update_yaxes(title_text='Price')

figB.show()


# In[ ]:





# In[ ]:




