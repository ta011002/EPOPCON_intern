import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data = [x1, x2, x3, x4]
group_lables = ['x1', 'x2', 'x3', 'x4']

fig = ff.create_distplot(hist_data, group_lables, bin_size=[.2, .1, .3, .4])

pyo.plot(fig, filename='Distplots(1).html')


* ### Snodgrass versus Twain
snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

hist_data = [snodgrass, twain]
group_lables = ['Snodgrass Writins', 'Mark Twain Writings']

fig = ff.create_distplot(hist_data, group_lables, bin_size=[0.005, 0.005])

pyo.plot(fig, filename='Distplots_Snod and Twain.html')