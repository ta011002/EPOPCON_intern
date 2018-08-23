#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######


# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# create a DataFrame from the .csv file:
df = pd.read_csv('../__data/mocksurvey.csv', index_col=0)
df


# create traces using a list comprehension:
data = [go.Bar(x=df.index, y=df[cols]) for cols in df.columns]

# Extra Credit
data = [go.Bar(x=df[cols], y=df.index, orientation='h') for cols in df.columns]


# create a layout, remember to set the barmode here
layout = go.Layout(title='Mock Survey Results', barmode='stack')


# create a fig from data & layout, and plot the fig.
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Bar Charts Exercise.html')