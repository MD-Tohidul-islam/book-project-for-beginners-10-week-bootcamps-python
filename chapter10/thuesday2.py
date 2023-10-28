import pandas as pd
#  build in methods
import random
random.seed(3)  # generate same random numbers every time, number used
#  does not matter
names = ['jess','jordan','sandy','ted','barney','tyler','rebecca']
ages = [random.randint(18,35) for x in range(len(names))]
people = {'ages':ages,'names':names}
df = pd.DataFrame.from_dict(people)
#   accessing the top 3 records using .head()

print(df.head(3))
print()

#  accessing the bottom 2 records using .tail()
print(df.tail(2))

#  accessing the column headers (keys) using the .keys() methods

headers = df.keys()
print(headers)

#  checking the shape, which is the number of records and columns
print(df.shape)

#  checking the general statistics of the Dataframe using .describe(),
#  only works on numerical columns
print(df.describe())

#  sort based on a given column, but keep the DataFrame in tact using
#  sort_values()
df2 = df.sort_values('ages')
print(df2.head(3))