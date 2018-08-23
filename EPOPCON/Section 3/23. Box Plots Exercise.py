#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######


# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np


# create a DataFrame from the .csv file:
df = pd.read_csv('../__data/abalone.csv')
df.head()


# take two random samples of different sizes:
np.random.seed(23)
random_a = np.random.choice(df['rings'], 50, replace=False)
random_b = np.random.choice(df['rings'], 30, replace=False)


# create a data variable with two Box plots:
data = [go.Box(y=random_a, name='random_a'),
        go.Box(y=random_b, name='random_b')]


# add a layout
layout = go.Layout(title='Compare random_a and random_b',
                    xaxis=dict(title='random_a'),
                    yaxis=dict(title='random_b'))


# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Box Plots Exercise.html')