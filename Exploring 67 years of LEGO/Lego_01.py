# Import modules
import pandas as pd

# Read colors data
colors = pd.read_csv('datasets/colors.csv')

# Print the first few rows
colors.head()

# How many distinct colors are available?
# -- YOUR CODE FOR TASK 3 --
num_colors = colors["rgb"].count()
#print(num_colors)

# colors_summary: Distribution of colors based on transparency
# -- YOUR CODE FOR TASK 4 --
#print(colors["is_trans"].head())

colors_summary =  colors.groupby(colors['is_trans']).count()
colors_summary

# Read sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')
# Create a summary of average number of parts by year: `parts_by_year`
parts = sets.groupby(sets['year']).mean()
#print(type(parts))
#print(parts.head())
parts_by_year = parts['num_parts']
#print(parts_by_year.head())
# Plot trends in average number of parts by year

import matplotlib.pyplot as plt

plt.plot(parts_by_year)
plt.xlabel("Year")
plt.ylabel("Number of parts")
plt.title("Average number of parts manufactured")
plt.show()

# themes_by_year: Number of themes shipped by year
# -- YOUR CODE HERE --
themes_by_year = sets.groupby(['year'], as_index=False).count().loc[:,['year', 'theme_id']]
#themes_by_year = year['theme_id']
print(themes_by_year.head())