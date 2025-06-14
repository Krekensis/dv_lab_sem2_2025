'''
1. For the MTCARS dataset, answer the specified questions with summarization and effective visuals.
a) Create a histogram to visualize the distribution of Miles Per Gallon (mpg).
b) Generate a boxplot for horsepower (hp) to identify outliers.
c) Plot a scatter plot between horsepower (hp) and mpg. What trend do you observe?
d) Create a bar chart showing the average mpg for each cylinder category (4, 6, 8 cylinders).
'''

import pandas as pd
import matplotlib.pyplot as mplot
import seaborn as sea

data = pd.read_csv('./Datasets/mtcars.csv')
print('\nInitial data:\n', data)

'''
for index, row in data.iterrows():
    if row['cyl'] == 4:
        print(row['mpg'])
'''
#a
mplot.figure(figsize=(8, 6))
sea.histplot(data.mpg, kde=True, color='#3d6aff') # KDE: Kernel Density Estimate
mplot.title('Distribution of mpg')
mplot.xlabel('Miles Per Gallon')
mplot.ylabel('Frequency')
mplot.savefig("./Lab 06 - DV plotting/Graphs/Q1_a_histogram.png")
mplot.show()

#b
mplot.figure(figsize=(8, 6))
sea.boxplot(data.hp, color='#3d6aff')
mplot.title('Boxplot for Horsepower (hp)')
mplot.xlabel('Horsepower (hp)')
mplot.ylabel('Values')
mplot.savefig("./Lab 06 - DV plotting/Graphs/Q1_b_boxplot.png")
mplot.show()

#c
mplot.figure(figsize=(15, 10))
sea.scatterplot(data, x=data.hp, y=data.mpg, hue='model', s=50)
mplot.title('Scatter plot between Horsepower (hp) and mpg', fontsize=20)
mplot.xlabel('Horsepower (hp)', fontsize=15)
mplot.ylabel('Miles Per Gallon (mpg)', fontsize=15)
mplot.tick_params(axis='both', which='major', labelsize=15)
mplot.savefig("./Lab 06 - DV plotting/Graphs/Q1_c_scatterplot.png")
mplot.show()

#d
avg_mpg = data.groupby('cyl')['mpg'].mean()
mplot.figure(figsize=(8, 6))
sea.barplot(x=avg_mpg.index, y=avg_mpg.values, palette='viridis')
mplot.title('Average mpg for each Cylinder Category')
mplot.xlabel('Cylinder Category')
mplot.ylabel('Average mpg')

for i, v in enumerate(avg_mpg.values):
    mplot.text(i, v, f'{v:.2f}', ha='center', va='bottom')

mplot.savefig("./Lab 06 - DV plotting/Graphs/Q1_d_barplot.png")
mplot.show()