import pandas as pd
import numpy as np
from platform import python_version
from numpy.ma.core import equal

# series = pd.Series([1,2,3,4,5]) # formats it as single column a list with an index (0-...) and shows dtype like excel

# we change the index with whatever name we want and give it a title using 'name'.

# series_updated = pd.Series([30,45,55], index=['2015 sales','2016 sales','2017 sales'], name="Product A")

# print(series_updated)
# data={'Name': ['Alice','bob','Charlie'],
#       'Age': [25,30,35],
#       'City':["New York",'Los Angeles','Chicago']}

# df = pd.DataFrame(data) # creates a dataframe with data thats 2d or has columns and rows

#print(df) # prints the 'data' in rows and columns with an index with their names at the top

# print(df.head(2)) # the head prints how many rows u want to see from the beginning of the df

# print(df.tail(2)) # the tail prints how many rows u want to see from the end of the df

# print(df.sample(2)) # the sample prints how many rows u want to see and chooses random rows from the df

# print(df.info()) # the info prints the information about each column of the entire df and how many rows it has, its type, etc

# print(df.describe()) # the describe prints the statistical info about the entire df numerical columns
                                                                # such as (count,mean,median,mode, etc)

# print(df.describe(include='object')) # the include = 'object' shows us the count, unique, top and freq of the non-numerical columns
# print(df.describe(include='all')) # the include = 'all' shows us everything about each row and columns nd stuff that doesnt
                                                            # match like non-numerical rows with mean will give 'NaN'

# print(df['Name'])//print(df.Name)  #prints only the column name
# print(df[df['Age']>30]) # u put an extra df around so it shows the entire column and row of the 'True' bool because
                                # df['Age']>30 only shows the bool so ur telling it to show everything else when adding df
# filtered_df = df[df['Age']>30]
# print(filtered_df)

# df['Salary'] = [70000,80000,90000] #if salary is not there it adds it automatically as a new column
# df['Age'] = df['Age']+1
# df['Salary'] = df['Salary']+5000
# print(df)
# df = df.drop('City',axis=1) # deletes the wanted name and axis=1 means delete the entire column and
                                                                            # axis=0 means delete the row
# print(df.head(2))











# df = pd.read_csv('employees.csv') # incase u dont know where the file is copy its entire path and paste it here,
                                                                                         # include a \ before it

# print(df.head(3))
# print(df.info())
# specialized_IT = df[df['Department'] == 'IT'] #// df[df.Department == 'IT']]
# print(specialized_IT)

# this is the aggregate function which is used alongside groupby to find, avg(),sum(),min(),max(),Count()...
# average_salary_by_dept = df.groupby('Department')['Salary'].mean()
# print("Average Salary By Department:\n")
# print(average_salary_by_dept)


# salary_increase = 0.05
# df['New_Salary_After_Raise'] = df['Salary']*salary_increase + df['Salary'] #// df['Salary']*1.05
# print(df.head(3))


# oldest_to_youngest = df.sort_values(by='Age',ascending=False) # ascending = false means highest to lowest
# print(oldest_to_youngest)


# employee_count_by_dept = df['Department'].value_counts().sort_values(ascending=False) # counts how many is in the chosen dataframe
# // x=df.groupby('Department')['Age'].count()
# print(employee_count_by_dept)


# df['Joining_Date'] = pd.to_datetime(df['Joining_Date']) #converts the wanted column to a datetime
# recent_joins = df[df['Joining_Date']>'2020-01-01']
# print("Employees Joined After 2020:\n")
# print(recent_joins)
# print(df.info())

# recent_joins.to_csv(r'recent_joins.csv',index=False)

reviews = pd.read_csv("winemag-data-130k-v2 (1).csv")
# print(reviews.head(4))
# print(reviews.price.dtype)
# print(reviews.sample())
# print(reviews.info())
# print(reviews.dtypes)
reviews.points=reviews.points.astype('float64') # this converts the ['points'] // .points column using astype into a float
                                                # instead of it being a int
# print(reviews.info())
# print(reviews.index.dtype) #dataframe or series index
# price = "100$"
# price = price.replace("$","") # replaces what u want in with the new one
# price = int(price)
# print(price)
# print(reviews.iloc[0,1])
# print(reviews.iloc[:,1])
# print(reviews.iloc[3:5,3:6]) # the iloc works as follows. 1) the first number is the index (which index we want) and
                               # the second number is which point of the row u want.

# print(reviews.iloc[8:10,2:5])
# print(reviews.iloc[13,12])
# print(reviews.iloc[:3, 0])
# print(reviews.iloc[6])
# print(reviews.head(7))
# print(reviews.iloc[1:3, 1])
# print(reviews.iloc[[0, 1, 2], 1])
# print(reviews.iloc[-5:])

# print(reviews.loc[0, 'country']) # the lock works as follows. 1) the first nuber is the index (which index we want) and the second
                                 # is the WORD we want to find in that column
# print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])
# print(reviews.iloc[15,1:6])



# print(reviews[pd.isnull(reviews.country)]) #// print(reviews[reviews.country.isnull()]) will bring out the empty or missing values
#                                            # of that wanted column

# print(reviews.region_2.fillna("Unknown")) # the fillna fills the NaN//missing values with what we want ('Unknown')

# reviews.region_2=reviews.region_2.replace(np.nan,"Unknown")

# reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
# print(python_version())





