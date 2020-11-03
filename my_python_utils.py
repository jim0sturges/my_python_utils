#!/usr/bin/env python
# coding: utf-8

# In[1]:


def create_test_data(start_date='20130101',num_cols=4,upper_bound=10,rnd=2,num_rows=20):
    import numpy as np
    '''
    Purpose: this module created a test data python dataframe of including a date column
    and n row and m columns (up to 26)random values from the “standard normal” distribution between
    0 and the upperbound.
    Input: start_date  - as a string 'yyyymmdd'
           num_cols    - integer less then 27 > 0
           num_rows    - integer > 0
           upper_bound - range for values from 0 to upper_bound
           rnd         - number of decimal points in values
    Output: data frame of nun=m_rows length with first column "date" followed by
            num_cols of random. The date column has been converted to string.
    '''
    colnames=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:num_cols]
    date=pd.DataFrame(pd.date_range(start_date,periods=num_rows)).rename(columns={0:'date'})
    df= pd.DataFrame(np.random.rand(num_rows, num_cols) * upper_bound,
                     columns=colnames).round(rnd)
    
    df = pd.concat([df, date], axis=1).set_index('date')
    df=df.reset_index().rename(columns={'index':'date'})
    df['date']=df['date'].dt.strftime('%Y-%m-%d')
    return(df)

def sxs(df,sxs_sets=2):
    '''
    Purpose: this module allows a dataframe to be display in wide format 
             by distributing the data in the number of side by side dataframes
             specified. It expects the first column to be a date
    Input:   a dataframe
    Output: ipython display of the dataframe in wide format 
    '''
    chunk=round((len(df)/sxs_sets))
    lst=[]
    for i in range(0,len(df),chunk):
        tmp_df=df.iloc[i:i+chunk]
        lst.append(tmp_df.reset_index(drop=True))
    display_df=lst[0]
    for i in range (1,len(lst)):
        display_df[i]=""
        display_df=pd.concat([display_df,lst[i]],axis=1)
    display_df=display_df.fillna("")
    for i in range(1,len(lst)):
        display_df=display_df.rename(columns={i:" "})
    display(display_df)    

#============================ test code for sxs =================================
#import pandas as pd
#import numpy as np 
#from IPython.display import display
#df=create_test_data(num_rows=31,num_cols=2)
#display(df)
#sxs(df,sxs_sets=3)    


    


# In[ ]:





# In[ ]:




