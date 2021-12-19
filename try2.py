import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from random import randint
import re

df = pd.read_csv(r'C:\Users\Mudit\Desktop\HW\Final\games.csv')

# There is no missing values, so we can proceed
#print(df.isnull().sum())

# To check if values in columns are saved in proper type
#print(df.dtypes)

# Preparing data

# Create new column which will contain the rating of two players
val = df['avg_rating'] = (df['white_rating']+df['black_rating'])/2
val2 = df['avg_rating'].describe()['min':'max']
#print(val)
#print(val2)

# as we can see min-max rating is 816-2475 so we can assign any game to some rating range and create new
# categorical column containing game level

r = (2500-800)/4
print(f'Lets say we have 4 levels \n')
lev_tab = ['low', 'mid', 'high', 'pro']
for x in range(0,4):
    print(lev_tab[x] + ' - ' + str(int(800+r*x)) + '-' + str(int(800+r*(x+1))))

# now we can analyze different aspects of dataframe based on game level

def fun(rat):
    for x in range(0,4):
        if rat >= 800+r*x and rat < 800+r*(x+1):
            return lev_tab[x]

val3=df['level'] = df['avg_rating'].apply(fun)
val4=df['level'].value_counts()
#print(val3)
#print(val4)
g = df.groupby(df['level']).mean()['turns'].sort_values().round()
print(g)

# as we can see the higher the level the game last longer

fig = px.histogram(g, x=g.index, y=g.values, histfunc='avg', labels={'y':'moves'} ,title='Average game lenght',
                   opacity=0.6, color=g.values, color_discrete_sequence=px.colors.sequential.Plasma_r)
fig.update_layout(bargap=0)
fig.show()

# we can also see scatter chart with avg rating value
fig = px.scatter(df, x='turns', y='avg_rating', color='level')
fig.show()

# Which color is victorious ?
df['count'] = 1
piv = pd.pivot_table(df, index='level',values='count', columns='winner',aggfunc='count')
df.drop(columns='count', axis=1)
piv

# Data Visualization
colors = ['black', 'lightgrey', 'white']

fig = make_subplots(rows=1, cols=4, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=piv.columns, values=piv.values[1], name='low'),1,1)
fig.add_trace(go.Pie(labels=piv.columns, values=piv.values[2], name='mid'),1,2)
fig.add_trace(go.Pie(labels=piv.columns, values=piv.values[0], name='high'),1,3)
fig.add_trace(go.Pie(labels=piv.columns, values=piv.values[3], name='pro'),1,4)

fig.update_traces(hole=.4, hoverinfo='label+percent+name', textfont_size=14,
                  marker=dict(colors=colors, line=dict(color='#F2F2F2', width=2)))

fig.update_layout(title_text="Victorious Color",
                  annotations=[dict(text='LOW', x=0.085, y=0.5, font_size=16, showarrow=False),
                               dict(text='MID', x=0.37, y=0.5, font_size=16, showarrow=False),
                               dict(text='HIGH', x=0.63, y=0.5, font_size=16, showarrow=False),
                               dict(text='PRO', x=0.91, y=0.5, font_size=16, showarrow=False)])
fig.show()

# How the games usually ends ?
s = df['victory_status'].value_counts()
fig = px.pie(s, values=s.values, names=s.index, color_discrete_sequence=px.colors.qualitative.Pastel)
fig.show()

# Victorious Status by game rating
t = pd.pivot_table(df, values='count', index='level', columns='victory_status',aggfunc='count')
fig = px.bar(t, color_discrete_sequence=px.colors.sequential.Agsunset, title = 'Victory Status By The Game Rating')
fig.show()

# lets take the most popular openings with variations
# Lets take the 30 most popular openings with variations
s = df['opening_name'].value_counts().head(30)
tab = '|'.join('^' + r"{}".format(x)+ '$' for x in s.index)
df_open = df.loc[df['opening_name'].str.contains(tab, regex=True)]
t = pd.pivot_table(df_open, values='count', columns='winner', index='opening_name', aggfunc='count').fillna(0)
g = df_open.groupby('opening_name').sum()['count']
tab = [[y/g.values[i] for y in x] for i,x in enumerate(t.values)]
fig = go.Figure(data=go.Heatmap(z=tab, x=t.columns, y=t.index, colorscale='plasma'))
fig.update_layout(title='Winner by the opening with variation in %', yaxis_nticks=50, margin=dict(t=60, r=20, b=10, l=20))
fig.show()

# Game Length by opening
g = df_open.groupby(by='opening_name').mean()['turns']
g = g.sort_values()
fig = px.bar(g.values, x=g.values, y=g.index, color=g.values)
fig.update_layout(title='Game lenght by the opening with variation', yaxis_nticks=50)
fig.show()

# Game Length by opening and length
df_open = df.copy()
df_open['opening_name'] = df_open['opening_name'].str.split(' ').str[0:2]
df_open['opening_name'] = df_open.opening_name.apply(lambda x: ' '.join([str(i).replace(':','') for i in x]))

s = df_open['opening_name'].value_counts()
s = s[s<30]
for x in s.index:
    df_open = df_open[~df_open.opening_name.str.contains(x)]
t = pd.pivot_table(df_open, values='turns' ,index='opening_name', columns='level', aggfunc='mean')
fig = go.Figure(data=go.Heatmap(z=t.values[0:31].round(),x=t.columns, y=t.index[0:31], colorscale="Inferno"))
fig.update_layout(title='Game Lenght by opening and level(part 1)', yaxis_nticks=200, margin=dict(t=80, r=200, b=0, l=200))
fig.show()

fig = go.Figure(data=go.Heatmap(z=t.values[31:62].round(),x=t.columns, y=t.index[31:62], colorscale="Inferno"))
fig.update_layout(title='Game Lenght by opening and level (part 2)', yaxis_nticks=200, margin=dict(t=80, r=200, b=0, l=200))
fig.show()

# as we can see we have some missing values, its because on the some game levels certain openings wasn't played at all

# check who wins on the depending of the opening
table = pd.pivot_table(df_open, values='count' ,index='opening_name', columns='winner', aggfunc='count').fillna(0)
g = df_open.groupby(['opening_name']).sum()['count']
tab = [x/g.values[i] for i,x in enumerate(table.values)]
fig = go.Figure(data=go.Heatmap(z=tab[0:31],x=table.columns, y=table.index[0:31], colorscale="Electric"))
fig.update_layout(title='Winner by opening and level (part 1)', yaxis_nticks=200, margin=dict(t=80, r=200, b=0, l=200))
fig.show()

fig = go.Figure(data=go.Heatmap(z=tab[31:62],x=table.columns, y=table.index[31:62], colorscale="Electric"))
fig.update_layout(title='Winner by opening (part 2)', yaxis_nticks=200, margin=dict(t=80, r=200, b=0, l=200))
fig.show()

# Adding levels to the same visualizations
def fun(o):
    if o == 'white':
        return 1
    elif o == 'draw':
        return 0
    else:
        return -1

df_open['win_points'] = df_open.winner.apply(fun)
table = pd.pivot_table(df_open, values='win_points' ,index=['opening_name'], columns='level', aggfunc='sum')
fig = go.Figure(data=go.Heatmap(z=table.values[0:31],x=table.columns, y=table.index[0:31], colorscale="Hot"))
fig.update_layout(title='Win by opening and level(part 1)', yaxis_nticks=200, margin=dict(t=80, r=200, b=0, l=200))
fig.show()

fig = go.Figure(data=go.Heatmap(z=table.values[31:62],x=table.columns, y=table.index[31:62], colorscale="Hot"))
fig.update_layout(title='Win by opening and level(part 2)', yaxis_nticks=200, margin=dict(t=80, r=200, b=0, l=200))
fig.show()

# as we can see negative values means that black is more likely to win

# Lets check how many book moves players play in case of game rating
df['opening_ply'].value_counts().sort_index()

# Lets take only the games which are longer than 20 moves and games of amount of opening moves equal or less than 20
df_open = df.loc[(df['opening_ply'] <= 20) &  (df['turns'] >= 20),['level', 'opening_ply']]

# To make this accurate we have to take % of every amount of moves separetly from every game level, because
# amount of games on diffrent levels is much diffrent

slow = df_open.loc[df_open['level']=='low',['opening_ply']].value_counts()
smid = df_open.loc[df_open['level']=='mid',['opening_ply']].value_counts()
shigh = df_open.loc[df_open['level']=='high',['opening_ply']].value_counts()
spro = df_open.loc[df_open['level']=='pro',['opening_ply']].value_counts()

slow, smid, spro, shigh = slow.sort_index()*100/slow.sum(), smid.sort_index()*100/smid.sum(), \
                          spro.sort_index()*100/spro.sum(), shigh.sort_index()*100/shigh.sum()
df_open = pd.DataFrame([spro.values, shigh.values, smid.values, slow.values],
                       columns=[str(x) for x in range(1,21)]).fillna(0)

# lets look at the cummulative Heatmap, because anybody who did e.g. 10 book moves also did it less

slow = slow.sort_index(ascending=False).cumsum().sort_index()
smid = smid.sort_index(ascending=False).cumsum().sort_index()
shigh = shigh.sort_index(ascending=False).cumsum().sort_index()
spro = spro.sort_index(ascending=False).cumsum().sort_index()
df_open = pd.DataFrame([spro.values, shigh.values, smid.values, slow.values],
                       columns=[str(x) for x in range(1,21)]).fillna(0)
fig = px.imshow(df_open, labels=dict(x="Number of Book Moves", y="Rating", color="%"),
                x=[x for x in range(1,21)], y=['pro','high','mid','low'])
fig.show()

# Lets take a look at the funnel chart, lets take firt 10 moves and another 10 seperatly to get a better view

y = df_open.columns.values[0:10]
fig = go.Figure()
fig.add_trace(go.Funnel(name='low',y=y, x=df_open.values[3][0:10], textinfo = 'percent total'))
fig.add_trace(go.Funnel(name='mid',y=y, x=df_open.values[2][0:10], textinfo = 'percent total'))
fig.add_trace(go.Funnel(name='high',y=y, x=df_open.values[1][0:10], textinfo = 'percent total'))
fig.add_trace(go.Funnel(name='pro',y=y, x=df_open.values[0][0:10], textinfo = 'percent total'))

fig.show()

y = df_open.columns.values[10:20]
fig = go.Figure()
fig.add_trace(go.Funnel(name='low',y=y, x=df_open.values[3][10:20], textinfo = 'percent total'))
fig.add_trace(go.Funnel(name='mid',y=y, x=df_open.values[2][10:20], textinfo = 'percent total'))
fig.add_trace(go.Funnel(name='high',y=y, x=df_open.values[1][10:20], textinfo = 'percent total'))
fig.add_trace(go.Funnel(name='pro',y=y, x=df_open.values[0][10:20], textinfo = 'percent total'))

fig.show()