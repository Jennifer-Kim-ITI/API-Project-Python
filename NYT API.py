#Import pandas package into python
import pandas as pd

#Sample data dictionary 
people_dataframe = [{'Name': 'Jen', 'Age': 20, 'City': 'New York'},
                    {'Name': 'Macy', 'Age': 38, 'City': 'Chicago'},
                    {'Name': 'Ryan', 'Age': 52, 'City': 'Los Angeles'},
                    {'Name': 'Chih', 'Age': 29, 'City': 'Seattle'},
                    {'Name': 'Eina', 'Age': 11, 'City': 'Atlanta'},
                    {'Name': 'Emily', 'Age': 67, 'City': 'New York'},
                    {'Name': 'Ashley', 'Age': 24, 'City': 'Memphis'}]

#Convert and reaname sample data to DataFrame 
df = pd.DataFrame.from_dict(people_dataframe)
print("This is the DataFrame that is going to be used for the exampeles below.")
print(df)
print("\n")

#Example 1: Filter Data 
#Purpose: Filter individuals aged 30 and above 
#Set a condition and then use boolean indexing to filter 
filtered_data = df[df['Age'] >= 30]

if not filtered_data.empty:
    print("List of people over the age of 30.")
    print(filtered_data)
else:
    print("No one is above the age 30.")

avg_age = df['Age'].mean() 
print(f"Average Age: {avg_age:}")
print("\n")

#Example 2: Age Order
#Purpose: Sorting the DataFrame by age in descending order
#Use the function 'sort_values' to sort the age column 
sorted_by_age_desc = df.sort_values(by='Age', ascending = False)

print("Order by age in descending order: ")
print(sorted_by_age_desc)
print("\n")

#Just put in for fun, same format as above but without ascending = False
sorted_by_age_asc = df.sort_values(by='Age')
print("Order by age in ascending order: ")
print(sorted_by_age_asc)
print("\n")

#Example 3: New Column 
#Purpose: Creating a new column, 'City Size' to categorize each city 
#Execute if-else statement using set cities to determine if it categorizes to 'Big City' or 'Small City'
df['City Size'] = ''

for index, row in df.iterrows():
    if row['City'] in ['New York', 'Los Angeles', 'Chicago']:
        df.at[index, 'City Size'] = 'Big City'
    else:
        df.at[index, 'City Size'] = 'Small City'

print("DataFrame with City Size:")
print(df)
print("\n")