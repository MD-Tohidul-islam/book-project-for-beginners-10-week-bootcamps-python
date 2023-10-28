import pandas as pd
#  creating dataframe
#  using the from dict method to convert a dictionary into a pandas dataframe
import random
random.seed(3)  # generate same random numbers every time, number used
#  does not matter
names = ['jess','jordan','sandy','ted','barney','tyler','rebecca']
ages = [random.randint(18,35) for x in range(len(names))]
people = {'ages':ages,'names':names}
df = pd.DataFrame.from_dict(people)
print(df)
#  accessing data by column
print(df['ages'])
print(df['ages'][3])  # select the value of 'ages' in the fourth row


#  indexing by record
#  directly selecting a record in pandas using .loc
print(df.loc[4])
print(df.loc[0]['names'])  # selecting the value at record 0 in the names column

#  slicing a dataframe
print(df[2:5])