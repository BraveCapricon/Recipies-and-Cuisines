import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df.head(5)) # Checking top 5 rows
print(df.tail(5)) # checking last 5 rows
print(df.dtypes) # checking datatype of the columns

#dropping some unnecessary columns
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors'], axis =1)
print(df.head(5))

# Renaming the column titles
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders":"Cylinders", "Transmission Type":"Transmission", "Driven_Wheels":"Drive Mode"})
print(df.head(5))

print(df.shape) # df.shape is a command to find the number of rows and columns in df dataframe

# To find the duplicated rows

df_dup_indeces=df.duplicated() # this returns a column (same size as df) of values either "True" or "False", where "True" means that the row/index is a duplicate of a previous row and "False" means its not a duplicate
print(df_dup_indeces)

df_clean=df.drop_duplicates()# this drops the duplicates, so it creates the dataframe without duplicates
print(df_clean)
print(df_clean.shape)

df_clean.to_csv('Output.txt', sep=',',index=False)
df_clean.to_csv('Output.csv', sep=',',index=False)

print(df_clean.count())

print(df_clean.isnull().sum()) # count missing values per column

df_clean2=df_clean.dropna() # this removes all rows with missing or null values
print(df_clean2.count())

print(df_clean2.isnull().sum()) # count missing values per column, zero null values, good

#Checking for outliers for each column using boxplot
sns.boxplot(x=df['HP'])
plt.show()

sns.boxplot(x=df['Cylinders'])
plt.show()

#Plot histogram

df_clean2.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5)) # the command is .value_counts(), and df_clean2.Make is the column name of the "Make" variable we want to plot, also nlargest(40), means the 40 largest "Make" values
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');
plt.show()

## Heat maps to show dependencies of variables
plt.figure(figsize=(10,5))
c= df_clean2.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
plt.show()

# Scatter plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['city mpg'])
ax.set_xlabel('HP')
ax.set_ylabel('MPG')
plt.show()

