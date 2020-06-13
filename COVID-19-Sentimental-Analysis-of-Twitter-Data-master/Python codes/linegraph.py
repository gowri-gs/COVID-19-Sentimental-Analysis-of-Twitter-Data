
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime
#df = pd.read_csv("C:\\Users\\HP\\Desktop\\docemo.csv")
df = pd.read_csv("docemo.csv")
val = df['doc']
print(type(val))
val1 = [df['sadness%'],df['joy%'],df['fear%'],df['disgust%'],df['anger%']]
#rint(val1)
title = 'sentiment analysis of covid 19 tweets'
labels = ['sadness', 'joy', 'fear', 'disgust', 'anger']
colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)', 'rgb(130,130,130)']

mode_size = [9, 9, 13, 9, 9]
line_size = [3, 3, 5, 3, 3]
'''''
x_data = np.array([['2020-04-01','2020-04-02','2020-04-03','2020-04-04','2020-04-05'],
                   ['2020-04-01','2020-04-02','2020-04-03','2020-04-04','2020-04-05'],
                   ['2020-04-01','2020-04-02','2020-04-03','2020-04-04','2020-04-05'],
                   ['2020-04-01','2020-04-02','2020-04-03','2020-04-04','2020-04-05'],
                   ['2020-04-01','2020-04-02','2020-04-03','2020-04-04','2020-04-05']])
'''
x_data = np.array([val,]*5)
print(x_data)
'''''
y_data = np.array([
    [30,40,0,10,20],
    [50,10,20,0,20],
    [25,30,30,15,10],
    [10,10,10,40,30],
    [20,40,30,10,0]
])
'''''
y_data = np.array(val1)
print(y_data)
fig = go.Figure()

for i in range(0,5):
    fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
        name=labels[i],
        line=dict(color=colors[i], width=line_size[i]),
        connectgaps=True,
    ))

    # endpoints
    fig.add_trace(go.Scatter(
        x=[x_data[i][0], x_data[i][-1]],
        y=[y_data[i][0], y_data[i][-1]],
        mode='markers',
        marker=dict(color=colors[i], size=mode_size[i])
    ))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white'
)

annotations = []

# Adding labels
for y_trace, label, color in zip(y_data, labels, colors):
    # labeling the left_side of the plot
    annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                  xanchor='right', yanchor='middle',
                                  text=label + ' {}%'.format(y_trace[0]),
                                  font=dict(family='Arial',
                                            size=16),
                                  showarrow=False))
    # labeling the right_side of the plot
    annotations.append(dict(xref='paper', x=0.95, y=y_trace[0],
                                  xanchor='left', yanchor='middle',
                                  text='{}%'.format(y_trace[0]),
                                  font=dict(family='Arial',
                                            size=16),
                                  showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='sentiment analysis of covid 19 tweets',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Source: Twitter',

                              font=dict(family='Arial',
                                        size=12,
                                        color='rgb(150,150,150)'),
                              showarrow=False))

fig.update_layout(annotations=annotations)

fig.show()
