

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Desktop\\docemo.csv")

#print(df['neu%'], df['pos%'], df['neg%'])

labels = ['neg%', 'pos%', 'neu%']
val = [df['neg%'].mean(), df['pos%'].mean(), df['neu%'].mean()]
colors = ['red', 'green', 'blue']
print(val[1])

fig = go.Figure(data=[go.Pie(labels=labels, values=val, marker=dict(colors=colors), pull=[0, 0.1, 0])])

fig.update_layout(
    title_text="OVERALL POLARITY SCORE", uniformtext_minsize=100,
    # Add annotations in the center of the donut pies
    annotations=[dict(text='POLARITY', x=0.5, y=0.5, font_size=40,  showarrow=False)])
fig.show()

