import pandas as pd

# Load the Excel files into Pandas DataFrames
df = pd.read_excel('Source.xlsx')
data = pd.read_excel('Scrap_รอบสอง_test.xlsx')

# Create a set of the places in the `source` DataFrame
condition = df['place'].tolist()

drop = []
drop_place = []
uniq_value = []
# Iterate over the rows in the `data` DataFrame
for i in range(len(data)):
    if i < len(data):
        # Get the value of the `place` column in the current row
        place = data.iloc[i, 0]

        # Check if the place is in the `condition` set
        if place not in condition:
            # If the place is not in the `condition` set, then delete the row
            drop.append(i)
            print("Not here")
            print(place)
            drop_place.append(place)
        else:
            print("Already have")


for value in drop_place:
    if value not in uniq_value:
        uniq_value.append(value)

data.drop(drop, inplace=True)
print(f"Total drop rows = : {len(drop)}")
print(f"Total unique values = {len(uniq_value)}")
print(uniq_value)
# data.to_excel('Scrap_รอบสอง_test.xlsx')

