import pandas as pd
import numpy as np


df = pd.read_csv("Employee.csv",encoding="latin1")

print(df.head())

#checking the missing values
print("Missing value in each coloumn")
print(df.isnull().sum())

#finding infinte values and replacing it into nan
df.replace([np.inf, -np.inf], np.nan,inplace=True)

#filling infinite values with mean values
df.fillna(df['ExperienceInCurrentDomain'].mean(),inplace=True)

#to remove duplicates records
df.drop_duplicates(inplace=True)


"""
if we change some employee data like having  salary column then

if salaries are in negative values
df["salary"] = np.where(df["salary"]<0 , df["salary"].mean(), df["salary"]
(this replaces the negative values with mean salary values)


if there are unrealistic or very large salary given in comparision to avg salary then how to fix it

 salary_mean  = df["salary"].mean()
 salary_std  = df["salary"].std()
#salary range
lower_bound = mean_salary - (3*lower_bound)
upper_bound = mean_salary + (3*upper_bound)  

#remove rows where salary is to high or to low
df = df[(df['salary'] >= lower_bound) & (df['salary'] <=upper_bound)]

"""

#now data is cleaned ,now we will save this file

df.to_csv("cleaned_employee",index=False)

print('data is cleaned and saved as "cleaned_employee"')

