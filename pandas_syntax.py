import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Days': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    'Months': ['Jan', 'Feb', 'March', 'April', 'May', 'Jun']
})

# print('******************************  Read Data Frame   *****************************\n')
# print(data)

file = pd.read_html('http://accessibility.psu.edu/tables/')

# print('\n*******************************  Read HTML   **********************************\n')

# print(file)

csv_file = pd.read_csv('E:/Sanat Documents/Python/hello.csv')

print('\n*******************************  Read CSV File   *******************************\n')

print(csv_file)

# print('\n*******************************  Read CSV File Head()  *******************************\n')

# print(csv_file.head())

# print('\n*******************************  Read CSV File Head(10)  *******************************\n')
# print(csv_file.head(10))

# print('\n*******************************  Read CSV File tail  *******************************\n')

# print(csv_file.tail())

print('\n*******************************  How many values are missing  *******************************\n')

#print(csv_file.isnull().sum())


