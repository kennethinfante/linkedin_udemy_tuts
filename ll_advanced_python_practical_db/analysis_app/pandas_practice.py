#%%
import pandas as pd

#%%
df = pd.read_csv('red30.csv')

#%%
df.head()

#%%
df.info()

#%%
df.describe()

#%%
df.ProdCategory.value_counts()

#%%
df['OrderType'].value_counts()

#%%
# for numerical vaues, describe may be better
df['OrderTotal'].describe()

#%%
df['Quantity'].hist()

#%%
df['ProdCategory'].value_counts().plot(kind='barh')

#%%
from sqlalchemy import create_engine

#%%
engine = create_engine("sqlite:///salespeople.sqlite")

#%%
# salespeople_df = pd.read_sql_table("salespeople", con=engine.connect(), index_col='idColumn', coerce_float=True, columns=["city", "state"], chunksize=250)
salespeople_df = pd.read_sql_table("salespeople", con=engine.connect())

#%%
salespeople_df.head()

#%%
salespeople_df['email_address'].head()

#%%
# do you need to import matplotlib here?
salespeople_df['state'].value_counts().plot(kind="barh")

#%%
engine = create_engine("sqlite:///landon.sqlite")

#%%
landon_df = pd.read_sql("sales", con=engine.connect(),index_col="order_id")

#%%
landon_df.sort_values("order_total")

#%%
landon_df['property_state'].value_counts()


#%%
import matplotlib.pyplot as plt

#%%
landon_top5 = landon_df['property_state'].value_counts().head(10)

#%%
plt.pie(landon_top5, labels=landon_top5.index.to_list())
