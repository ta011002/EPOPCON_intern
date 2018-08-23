#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######


# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd


# create a DataFrame from the .csv file:
df = pd.read_csv('../__data/iris.csv')
df.head()


# Define the traces

iris_sp = list(df['class'].unique())
hist = dict()
for i in range(len(iris_sp)):
    hist['traice{}'.format(i)] = df[df['class']==iris_sp[i]]['petal_length']

# HINT:
# This grabs the petal_length column for a particular flower
#df[df['class']=='Iris-some-flower-class']['petal_length']


# Define a data variable
hist_data = list(hist.values())
group_lables = iris_sp.copy()


# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_lables)

pyo.plot(fig, filename='DistPlots Exercise.html')