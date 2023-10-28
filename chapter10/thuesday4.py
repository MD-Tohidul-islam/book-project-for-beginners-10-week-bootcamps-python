import pandas as pd
#  build in methods
import random
random.seed(3)  # generate same random numbers every time, number used
#  does not matter
names = ['jess','jordan','sandy','ted','barney','tyler','rebecca']
ages = [random.randint(18,35) for x in range(len(names))]
people = {'ages':ages,'names':names}
df = pd.DataFrame.from_dict(people)
#  generating a new column with data
random.seed(321)
tenure = [random.randint(0,10) for x in range(len(df))]
df['tenure'] = tenure  # same as adding a new ket-value pair in a dictionary
print(df.head())
def ageGroup(age):
    return 'Teenager' if age <21 else 'Adult'
df['age_group'] = df['ages'].apply(ageGroup)

#  aggregations
#  groupby()
#  gouping the records together to count how many records in each group
print(df.groupby('age_group', as_index=False).count().head())
print()
#  grouping the data to see averages of all columns
print(df.groupby('age_group',as_index=False).mean().head())
print()
#  group-by() with multiple columns
#  grouping information by their age group, then by their tenure
print(df.groupby(['age_group','tenure'],as_index=False).count().head(10))
print()
#  adding a record to the bottom of the DataFrame
df.loc[7] = [25,'jess',2,'Adult']  # add a record
print(df.head(10))
print()
#  removing duplicates based on same names
df = df.drop_duplicates(subset='names')
print(df.head(10))
print()


#  creating a second DataFrame
ratings = {
    'names':['jess','tyler','ted'],
    'ratings':[10,9,6]
}
ratings = df.from_dict(ratings)
print(ratings.head())
print()
# inner Join
#  performing an inner join with our df and ratings DataFrames based on
#  names, het data that matches
matched_ratings = df.merge(ratings,on = 'names',how='inner')
print(matched_ratings.head())
print()
#  performing an outer join with our df and ratings DataFrames based on
#  names , get all data
all_ratings = df.merge(ratings,on='names',how='outer')
print(all_ratings.head())