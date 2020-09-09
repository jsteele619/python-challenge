#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data_file = "Resources/budget_data.csv"
budget = pd.read_csv(data_file)


# In[2]:


budget_months = budget["Date"].value_counts()
budget_profit = budget["Profit/Losses"]


# In[3]:


changelist = []
for x in range(85):
    change = budget_profit[x+1] - budget_profit[x]
    changelist.append(change)


# In[4]:


datelist = []
for x in range(85):
    if budget.iloc[x+1,1] - budget.iloc[x,1] == max(changelist):
        date = budget.iloc[x+1,0]
        datelist.append(date)


# In[5]:


datelist2 = []
for x in range(85):
    if budget.iloc[x+1,1] - budget.iloc[x,1] == min(changelist):
        date = budget.iloc[x+1,0]
        datelist2.append(date)


# In[6]:


print("Here are my solutions!")
print("Total Months:", len(budget_months))
print("Total Net:", sum(budget_profit))
print("Average  Change:", budget_profit.mean())
print("Greatest Increase in Profits:", datelist, max(changelist))
print("Greatest Decrease in Profits:", datelist2, min(changelist))


# In[13]:


f = open("final.txt","a+")
f.write("\nHere are my solutions!\n")
f.write("Total Months: ")
f.write(str(len(budget_months)))         
f.write("\nTotal Net: ")
f.write(str(sum(budget_profit)))   
f.write("\nAverage  Change: ")
f.write(str(budget_profit.mean()))
f.write("\nGreatest Increase in Profits: ")
f.write(str(datelist ))
f.write(str(max(changelist)))
f.write("\nGreatest Decrease in Profits: ")
f.write(str(datelist2) )
f.write(str(min(changelist)) )
f.close() 


# In[ ]:





# In[ ]:




