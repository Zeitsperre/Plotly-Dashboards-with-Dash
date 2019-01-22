#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import math

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mpg.csv')
print(df.columns)

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg']*0.425144,
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['cylinders']*math.e,
                               color=df['cylinders'],
                               showscale=True))]

# create a layout with a title and axis labels
layout = go.Layout(title='MPG Data',
                   xaxis=dict(title='Horsepower', titlefont=dict(family='Courier New, monospace', size=20, color='black')),
                   yaxis=dict(title='Km/L', showticklabels=True, titlefont=dict(family='Courier New, monospace', size=20, color='black')))

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, )
pyo.plot(fig)
