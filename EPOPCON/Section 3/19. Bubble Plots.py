import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../__data/mpg.csv')
df.head()


# size of the cylinders
data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(size=2*df['cylinders']))]

layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Bubble Plots_cylinders.html')


# size of the weight
data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(size=df['weight']/100,
                                color=df['cylinders'],
                                showscale=True))]

layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Bubble Plots_weight.html')