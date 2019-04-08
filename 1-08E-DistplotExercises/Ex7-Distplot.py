#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../Data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.figure_factory as ff
import plotly.offline as pyo
import numpy as np
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/iris.csv')

# Define the traces
setosa = df[df['class']=='Iris-setosa']['petal_length']
versicolor = df[df['class']=='Iris-versicolor']['petal_length']
virginica = df[df['class']=='Iris-virginica']['petal_length']

# HINT:
# This grabs the petal_length column for a particular flower
# df[df['class']=='Iris-some-flower-class']['petal_length']

# Define a data variable
data = [setosa, versicolor, virginica]
layout = ['setosa', 'versicolor', 'virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(data, layout)
pyo.plot(fig)
