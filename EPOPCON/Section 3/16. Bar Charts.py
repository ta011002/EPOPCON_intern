import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../__data/2018WinterOlympics.csv')
df.head()

trace1 = go.Bar(x=df['NOC'], y=df['Gold'],
                name='Gold', marker={'color':'#FFD700'})

trace2 = go.Bar(x=df['NOC'], y=df['Silver'],
                name='Silver', marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'], y=df['Bronze'],
                name='Bronze', marker={'color':'#CD7F32'})


data = [trace1, trace2, trace3]

layout = go.Layout(title='Medals', barmode='stack') # nested bar chart 를 출력하기 위해서는
                                                    # barmode는 삭제하여 default 값인 None 값으로 하여 출력한다.
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Bar Charts.html')