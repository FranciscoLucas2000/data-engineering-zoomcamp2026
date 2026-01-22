#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'


# In[10]:


df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)


# In[26]:


url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'


# In[11]:


df.head()


# In[12]:


df.tail()


# In[13]:


df.shape


# In[14]:


df.dtypes


# In[8]:


df.describe()


# In[16]:


df['tpep_pickup_datetime']


# In[18]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[19]:


df.head()


# In[21]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[22]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[23]:


df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[24]:


len(df)


# In[34]:


get_ipython().system('uv add tqdm')


# In[37]:


from tqdm.auto import tqdm


# In[27]:


df_iter = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)


# In[39]:


for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


# In[31]:


df = next(df_iter)


# In[33]:


df


# In[ ]:




