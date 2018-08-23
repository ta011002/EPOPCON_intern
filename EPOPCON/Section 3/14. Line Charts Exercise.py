#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######


# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../__data/2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

df = df[df.columns[1:]]
df.head()

# Use a for loop (or list comprehension to create traces for the data list)

# not use comprehension
data = []

for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter(x=df[df['DAY'] == day]['LST_TIME'],
                       y=df[df['DAY'] == day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)

# use comprehension
data = [go.Scatter(x=df[df['DAY'] == day]['LST_TIME'],
                   y=df[df['DAY'] == day]['T_HR_AVG'],
                   mode='lines',
                   name=day) for day in days]

# Define the layout
layout = go.Layout(title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
                   hovermode='closest')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Line Charts Exercise.html')