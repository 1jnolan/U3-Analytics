import pandas as pd
import pygal

"""
#************************************
#STAGE 1 - CLEANING THE FILE
#************************************

data_file = pd.read_csv('Journeys_2024_2025.csv')

#filter/isolate specific data.
filtered_data = data_file[['TravelDate','TubeJourneyCount']]

#write the filtered data to a new CSV file.- we are only doing this to try and make it more manageable. It doesn't really clean the data.
filtered_data.to_csv('tube_journeys_cleaned.csv', index=False)
"""


#************************************
#STAGE 2 working with the data wanted:
#************************************

data_file = pd.read_csv('tube_journeys_cleaned.csv') #using pandas, read in the CSV file into a dataframe (here I called it data_file)
#print(data_file) #I printed the file to take a look at the data before editing further.


#************************************
"""Long Version:"""
#************************************

#1. Isolate a specific column:
date_column = data_file['TravelDate']

#2 Convert the ints to strings:
dates_to_strings = date_column.astype(str)

#3 Check the rows that start with 2025:
is_2025 = dates_to_strings.str.startswith('2025')

#4 is_2025 will now have a list of True/False stored in it
#this aligns with the dates list.
#Use this data to make the new list:
filtered_data = data_file[is_2025]

#5 Make a copy of the data that meets what we need -
df_2025 = filtered_data.copy()

#6 Do what you need to wuth the data:
print("Number of rows found for 2025:", len(df_2025))

#************************************
#Short version:
#************************************

#FILTERING DATA TO ONLY RETURN 2025 JOURNEYS
"""
When I tried this in class on Tuesday, I tried to isolate it based on the start of the
data 2025 - but, python found ints and couldn't do this, so instead I have converted each item in the
column TravelDate from an int to a string:
"""

#SHORT VERSION HERE:
df_2025 = data_file[data_file['TravelDate'].astype(str).str.startswith('2025')].copy()

"""
Explanation:

(.astype(str)) - this changes the int to a string
(.str.startswith('2025')) - this looks at each row and checks if it starts with 2025
(.copy()) - this creates a new copy of the filtered data. I cannot remember why this is import!
"""

# 3. Select the data from the 'TubeJourneyCount' column
journey_data = df_2025['TubeJourneyCount']

# 4. Calculate the required statistics
median_val = journey_data.median()
mean_val = journey_data.mean()
# Mode returns a Series (in case of ties), so we convert it to a list
mode_val = journey_data.mode().tolist()
max_val = journey_data.max()
min_val = journey_data.min()

# 5. Calculate the frequency (count) of the min and max values
# This counts how many times the exact min or max value appears in the 2025 data
freq_min = (journey_data == min_val).sum()
freq_max = (journey_data == max_val).sum()

# 6. Display the results using comma separation to avoid f-strings and { brackets
print("Statistics for 2025")
print("Median journeys:", median_val)
