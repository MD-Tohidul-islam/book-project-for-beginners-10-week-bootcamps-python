import pandas as pd
#  build in methods
import random
random.seed(3)  # generate same random numbers every time, number used
#  does not matter
names = ['jess','jordan','sandy','ted','barney','tyler','rebecca']
ages = [random.randint(18,35) for x in range(len(names))]
people = {'ages':ages,'names':names}
df = pd.DataFrame.from_dict(people)

#  using a conditional to create a true/false column to work with
can_drink = df['ages'] > 21
print(can_drink)

#  using sub-setting to filter out records and keep DatraFrame intact
df2 = df[df['ages'] > 21]
print(df2)
#  generating a new column with data
random.seed(321)
tenure = [random.randint(0,10) for x in range(len(df))]
df['tenure'] = tenure  # same as adding a new ket-value pair in a dictionary
print(df.head())

#  apply()
#  feature engineering a new column from known data using a UDF
def ageGroup(age):
    return 'Teenager' if age <21 else 'Adult'
df['age_group'] = df['ages'].apply(ageGroup)
print(df.head(3))