import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import matplotlib.animation as animation
from IPython.display import HTML
import time
df1=pd.read_excel("D:\\如果RNN会说话\\素材_01.xlsx")
temp=[]
for i in range(df1["发布时间"].shape[0]):
    temp.append(str(df1["发布时间"][i]))
df=pd.DataFrame()
df["主题"]=df1["主题"]
df["发布时间"]=temp
df["微博数"]=df1["微博数"]
df["转发数"]=df1["转发数"]
df["评论数"]=df1["评论数"]
df["点赞数"]=df1["点赞数"]
import random
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color
color_list=[]
for i in range(len(list(df["主题"].unique()))):
    b=randomcolor()
    color_list.append(b)
colors = dict(zip(
    list(df1["主题"].unique()),color_list
))
fig, ax = plt.subplots(figsize=(15, 8))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def draw_barchart(year):
    dff = df[df['发布时间'].eq(year)].sort_values(by='微博数', ascending=True)
    ax.clear()
    ax.barh(dff['主题'], dff['微博数'],color=[colors[x] for x in dff['主题']])
    dx = dff['微博数'].max() / 200
    for i, (weiboshu,zhuti) in enumerate(zip(dff['微博数'], dff['主题'])):
        ax.text(weiboshu-dx, i,     zhuti,           size=14, weight=600, ha='right', va='bottom')
        ax.text(weiboshu+dx, i,     weiboshu,  size=14, ha='left',  va='center')
    # ... polished styles
    ax.text(1, 0.1, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, '条数', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, '不同主题热度（微博数）',
            transform=ax.transAxes, size=24, weight=600, ha='left')
#     ax.text(1, 0, 'by QIML', transform=ax.transAxes, ha='right',
#             color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
import datetime
frame=[]
begin = datetime.date(2021,3,10)
end = datetime.date(2021,4,20)
for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)
    for i in range(12):
        if i<5:
            frame.append(str(day)+" 0"+str(2*i)+":00:00")
        else:
            frame.append(str(day)+" "+str(2*i)+":00:00")
import matplotlib.animation as animation
from IPython.display import HTML
fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=frame,interval=100)
HTML(animator.to_jshtml()) 
animator.save('D:\\如果RNN会说话\\微博数动态条形图.gif',writer='pillow')


fig, ax = plt.subplots(figsize=(15, 8))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def draw_barchart(year):
    dff = df[df['发布时间'].eq(year)].sort_values(by='转发数', ascending=True)
    ax.clear()
    ax.barh(dff['主题'], dff['转发数'],color=[colors[x] for x in dff['主题']])
    dx = dff['转发数'].max() / 200
    for i, (weiboshu,zhuti) in enumerate(zip(dff['转发数'], dff['主题'])):
        ax.text(weiboshu-dx, i,     zhuti,           size=14, weight=600, ha='right', va='bottom')
        ax.text(weiboshu+dx, i,     weiboshu,  size=14, ha='left',  va='center')
    # ... polished styles
    ax.text(1, 0.1, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, '条数', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, '不同主题转发数',
            transform=ax.transAxes, size=24, weight=600, ha='left')
#     ax.text(1, 0, 'by QIML', transform=ax.transAxes, ha='right',
#             color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
import datetime
frame=[]
begin = datetime.date(2021,3,10)
end = datetime.date(2021,4,20)
for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)
    for i in range(12):
        if i<5:
            frame.append(str(day)+" 0"+str(2*i)+":00:00")
        else:
            frame.append(str(day)+" "+str(2*i)+":00:00")
import matplotlib.animation as animation
from IPython.display import HTML
fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=frame,interval=100)
HTML(animator.to_jshtml()) 
animator.save('D:\\如果RNN会说话\\转发数动态条形图.gif',writer='pillow')



fig, ax = plt.subplots(figsize=(15, 8))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def draw_barchart(year):
    dff = df[df['发布时间'].eq(year)].sort_values(by='评论数', ascending=True)
    ax.clear()
    ax.barh(dff['主题'], dff['评论数'],color=[colors[x] for x in dff['主题']])
    dx = dff['评论数'].max() / 200
    for i, (weiboshu,zhuti) in enumerate(zip(dff['评论数'], dff['主题'])):
        ax.text(weiboshu-dx, i,     zhuti,           size=14, weight=600, ha='right', va='bottom')
        ax.text(weiboshu+dx, i,     weiboshu,  size=14, ha='left',  va='center')
    # ... polished styles
    ax.text(1, 0.1, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, '条数', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, '不同主题评论数',
            transform=ax.transAxes, size=24, weight=600, ha='left')
#     ax.text(1, 0, 'by QIML', transform=ax.transAxes, ha='right',
#             color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
import datetime
frame=[]
begin = datetime.date(2021,3,10)
end = datetime.date(2021,4,20)
for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)
    for i in range(12):
        if i<5:
            frame.append(str(day)+" 0"+str(2*i)+":00:00")
        else:
            frame.append(str(day)+" "+str(2*i)+":00:00")
import matplotlib.animation as animation
from IPython.display import HTML
fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=frame,interval=100)
HTML(animator.to_jshtml()) 
animator.save('D:\\如果RNN会说话\\评论数动态条形图.gif',writer='pillow')






fig, ax = plt.subplots(figsize=(15, 8))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def draw_barchart(year):
    dff = df[df['发布时间'].eq(year)].sort_values(by='点赞数', ascending=True)
    ax.clear()
    ax.barh(dff['主题'], dff['点赞数'],color=[colors[x] for x in dff['主题']])
    dx = dff['点赞数'].max() / 200
    for i, (weiboshu,zhuti) in enumerate(zip(dff['点赞数'], dff['主题'])):
        ax.text(weiboshu-dx, i,     zhuti,           size=14, weight=600, ha='right', va='bottom')
        ax.text(weiboshu+dx, i,     weiboshu,  size=14, ha='left',  va='center')
    # ... polished styles
    ax.text(1, 0.1, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, '条数', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, '不同主题点赞数',
            transform=ax.transAxes, size=24, weight=600, ha='left')
#     ax.text(1, 0, 'by QIML', transform=ax.transAxes, ha='right',
#             color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
import datetime
frame=[]
begin = datetime.date(2021,3,10)
end = datetime.date(2021,4,20)
for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)
    for i in range(12):
        if i<5:
            frame.append(str(day)+" 0"+str(2*i)+":00:00")
        else:
            frame.append(str(day)+" "+str(2*i)+":00:00")
import matplotlib.animation as animation
from IPython.display import HTML
fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=frame,interval=100)
HTML(animator.to_jshtml()) 
animator.save('D:\\如果RNN会说话\\点赞数动态条形图.gif',writer='pillow')