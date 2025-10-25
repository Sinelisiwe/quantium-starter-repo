import csv
import pandas as pd

df = pd.concat(map(pd.read_csv, ['/Users/sinelisiwesibeko/PycharmProjects/quantium-starter-repo/data/daily_sales_data_0.csv', '/Users/sinelisiwesibeko/PycharmProjects/quantium-starter-repo/data/daily_sales_data_1.csv', '/Users/sinelisiwesibeko/PycharmProjects/quantium-starter-repo/data/daily_sales_data_2.csv']), ignore_index=True)

mask = df['product'] == 'pink morsel'
df = df[mask]

df['price'] = df['price'].str.replace('$','')
df['price'] = df['price'].astype('float')

df['Sales'] = df['price'] * df['quantity']
df['Date'] = df['date'].astype('datetime64[ns]')
df['Region'] = df['region'].astype('str')

df.pop('product')
df.pop('price')
df.pop('quantity')
df.pop('date')
df.pop('region')

print(df)


