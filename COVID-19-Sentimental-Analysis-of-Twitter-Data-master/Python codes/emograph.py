
import pandas as pd
import plotly.express as px
import csv
#df = pd.read_csv("C:\\Users\\HP\\Desktop\\catop.csv")
df = pd.read_csv("catop.csv")
#print(df)

result = df.groupby('cat_label').mean()

#result.to_csv("C:\\Users\\HP\\Desktop\\result1.csv")
#df1 = pd.read_csv("C:\\Users\\HP\\Desktop\\result1.csv")
result.to_csv("result1.csv")
df1 = pd.read_csv("result1.csv")


fig = px.bar(df1, y='cat_score', x='cat_label',text='cat_score')
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(title_text="Category Graph",uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()

