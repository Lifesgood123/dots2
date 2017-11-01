import plotly.plotly as py
import plotly.graph_objs as go

labels = ['Work', 'Sleep', 'school', 'Driving', 'Rec']
count = 0
values = [37, 52.5, 9.5, 3.5, 64.5]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='weekly')