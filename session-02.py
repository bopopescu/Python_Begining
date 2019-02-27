import pandas as pd
import numpy as np

df = pd.read_csv('E:/Sanat Documents/Python/BL-Flickr-Images-Book.csv')
# print(csv_file)

print('******************************* Print Full CSV File ************************')
print(df.head())

print('******************************* Drop specific column  ************************')
to_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors',
           'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(to_drop, inplace=True, axis=1)
print(df.head())

print('******************************* Changing the Index of a DataFrame  ************************')
print(df['Identifier'].is_unique)
df = df.set_index('Identifier')
print(df.head())

print('\n\n*********** access each record in a straightforward way   ****************\n*********** Row Access by loc command *****************\n')
print(df.loc[472])
print('************************ Row Access by iloc command  ************************')
print(df.iloc[0])

print('\n\n******************************* Tidying up Fields in the Data  ************************')
print('****we will be cleaning Date of Publication and Place of Publication.*****')
print(df.get_dtype_counts())
print(df.loc[1905:, 'Date of Publication'].head(10))

print('****  Remove the extra dates, Convert date ranges to their “start date”, *****')
extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
print(extr.head())
df['Date of Publication'] = pd.to_numeric(extr)
print(df['Date of Publication'].dtype)

print(df['Date of Publication'].isnull().sum() / len(df))