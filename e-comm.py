import pandas as pd
pd.set_option('display.max_columns', None)
df_sale = pd.read_csv("E-commerece sales data 2024.csv")
df_customer = pd.read_csv("customer_details.csv")
df_product = pd.read_csv("product_details.csv")

df_sale['user id'] = df_sale['user id'].apply(lambda x: str(int(x)) if pd.notna(x) else None)
df_customer['Customer ID'] = df_customer['Customer ID'].astype(str)

df_merged1 = df_sale[['user id', 'product id', 'Interaction type', 'Time stamp']].merge(df_customer, left_on = 'user id', right_on = 'Customer ID', how="left")
df_merged = df_merged1.merge(df_product[['Uniqe Id', 'Product Name', 'Category', 'Selling Price','Shipping Weight','Is Amazon Seller']], left_on = 'product id', right_on = 'Uniqe Id', how = 'left' )

df_cleaned = df_merged[df_merged['product id'].notna()]
df_cleaned['Time stamp'] = pd.to_datetime(df_cleaned['Time stamp'], dayfirst = True, errors = 'coerce')
df_cleaned['Order date'] = df_cleaned['Time stamp'].dt.date
df_cleaned.to_csv("grouped_and_cleaned.csv", index=False, encoding="utf-8-sig")
