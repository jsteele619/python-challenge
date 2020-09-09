#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd
data_file = ("resources/election_data.csv")
election = pd.read_csv(data_file)


# In[80]:


candidates = election[["Candidate"]]

candidates_vote = (election["Candidate"].unique())


# In[81]:


candidates_values = candidates.value_counts()
candidates_sum = pd.DataFrame({"Number of Votes": candidates_values, "Percentage": candidates_values/len(candidates)})


# In[82]:


print("The number of voters this year is", len(candidates)) 
print("The candidates this year are", candidates_vote)
print("The results this year:")
print(candidates_sum)
print("The winner is Khan")


# In[100]:


f = open("final.txt","a+")
f.write("\nThe number of voters this year are ")
f.write(str(len(candidates)))
f.write("\nThe candidates this year are") 
f.write(str(candidates_vote))
f.write("\nThe results this year:\n") 
f.write(str(candidates_sum))
f.write("\n\nThe winner is Khan")
f.close() 


# In[35]:





# In[50]:





# In[56]:





# In[ ]:




