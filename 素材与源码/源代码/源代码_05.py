import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import cpca
import seaborn as sns
import time

from snownlp import SnowNLP
from snownlp import sentiment
from snownlp.sentiment import Sentiment

def get_sentiments(text):
    try:
        s = SnowNLP(text)
        return s.sentiments
    except:
        return 0

def get_keywords(text):
    s = SnowNLP(text)
    return s.keywords(3)

def get_summary(text):
    s = SnowNLP(text)
    return s.summary(3)

def concat_func(x):
    return pd.Series({
        '微博正文':','.join(x['微博正文'].unique())
    })

#数据统计
file_name_lst=['新疆棉','HM','优衣库','耐克','阿迪达斯','匡威']
file_name_lst_in=['素材_03','素材_04','素材_08','素材_07','素材_06','素材_05']
df_list=[]

for i in range(len(file_name_lst_in)):
    print(file_name_lst[i])
    df=pd.read_csv("D:\\如果RNN会说话\\"+file_name_lst_in[i]+".csv")
    # 过滤
    searchfor = ['全棉时代','￥','红豆','押题','刷题','答题','证券从业','唱吧','抽','奖','健身','减肥','考试','房','室','厅','信用','游戏']
    df = df[~df['微博正文'].str.contains('|'.join(searchfor))]
    #加地理
    df_add=cpca.transform(df['发布位置'])
    df[['省','市','区','地址','adcode']]=df_add[['省','市','区','地址','adcode']]
    df=df[['微博正文','发布位置','话题','转发数','评论数','点赞数','发布时间','省','市']]
    df['发布时间']=df['发布时间'].apply(pd.to_datetime)
    df.to_csv("D:\\如果RNN会说话\\"+file_name_lst[i]+"地理.csv", index=False, encoding="utf_8_sig")
    #时间聚合
    df1=df[['转发数','评论数','点赞数','发布时间']]
    df1=df1.set_index('发布时间',drop=True)
    df2=df1.resample('D').sum()# D
    df3=pd.DataFrame()
    df3['微博数']=df1['转发数'].resample('D').count()
    df3=df3.reset_index()
    df2=df2.reset_index()
    df_result=pd.merge(df3,df2,on='发布时间')
    df_result.sort_values("发布时间",inplace=True)
    #并文本
    df4=df[['发布时间','微博正文']].replace(np.nan, '', regex=True)
    df4=df[['发布时间','微博正文']].replace(np.nan, '', regex=True)
    df4['发布时间']=df4['发布时间'].apply(pd.to_datetime)
    df4=df4.set_index('发布时间')
    df5=df4.groupby(pd.Grouper(freq='D')).apply(concat_func).reset_index()
    
    #正文情感分
    df5["正文情感分"] = df5["微博正文"].apply(get_sentiments)
    df_result=pd.merge(df_result,df5[['发布时间','正文情感分']],on='发布时间')
    df_result["正文情感分"]=(df_result["正文情感分"]-0.5)*2
    df_fill = (df_result.set_index('发布时间')
        .reindex(pd.date_range("20210310", "20210420", freq='D')))
    df_fill['微博数'].interpolate(inplace=True)
    df_fill['转发数'].interpolate(inplace=True)
    df_fill['评论数'].interpolate(inplace=True)
    df_fill['点赞数'].interpolate(inplace=True)
    df_fill['正文情感分'].interpolate(inplace=True)
    df_fill=df_fill.reset_index()
    df_fill = df_fill.rename({'index': '发布时间'}, axis=1)
    df_list.append(df_fill)
df_delta=df_list.copy()

    #累计值
    df_cumsum=pd.DataFrame()
    df_cumsum['微博数']=df_fill['微博数'].cumsum()
    df_cumsum['转发数']=df_fill['转发数'].cumsum()
    df_cumsum['评论数']=df_fill['评论数'].cumsum()
    df_cumsum['点赞数']=df_fill['点赞数'].cumsum()
    df_cumsum['正文情感分']=df_fill['正文情感分'].cumsum()
    df_cumsum['发布时间']=df_fill['发布时间']
    df_cumsum['主题']=file_name_lst[i]
    df_result_merge=df_result_merge.append(df_cumsum,ignore_index=True)
    
    df_result_merge = df_result_merge.sort_values(["主题", "发布时间"], ascending = (True, True))
    df_list.append(df_result_merge)
df_accum=df_list.copy()

df_pic_data=[]
for i in range(len(pic_name_lst)):
    df_temp=pd.DataFrame(columns=['发布时间',pic_name_lst[i],'主题'])
    for j in range(len(file_name_lst)):
        df=pd.DataFrame()
        df['发布时间']=df_delta[j]['发布时间']
        df[pic_name_lst[i]]=df_delta[j][pic_name_lst[i]]
        df['主题']=file_name_lst[j]
        df_temp=df_temp.append(df)
    #图
    print(pic_name_lst[i])
    plt.figure(i)
    ax =sns.lineplot(data=df_temp, x="发布时间", y=pic_name_lst[i], hue="主题")
    ax.tick_params(axis="x", rotation=90)
    ax.set_xticks(['2021-03-10','2021-03-13','2021-03-16',
                    '2021-03-19','2021-03-21','2021-03-24',
                    '2021-03-27','2021-03-30','2021-04-02',
                    '2021-04-05','2021-04-08','2021-04-11',
                    '2021-04-14','2021-04-17','2021-04-20'])

df_pic_data=[]
for i in range(len(pic_name_lst)):
    df_temp=pd.DataFrame(columns=['发布时间',pic_name_lst[i],'主题'])
    for j in range(len(file_name_lst)):
        df=pd.DataFrame()
        df['发布时间']=df_accum[j]['发布时间']
        df[pic_name_lst[i]]=df_accum[j][pic_name_lst[i]]
        df['主题']=file_name_lst[j]
        df_temp=df_temp.append(df)
    #图
    print(pic_name_lst[i])
    plt.figure(i)
    ax=sns.lineplot(data=df_temp, x="发布时间", y=pic_name_lst[i], hue="主题",err_style='bars',ci=0)
    ax.tick_params(axis="x", rotation=90)
    ax.set_xticks(['2021-03-10','2021-03-13','2021-03-16',
                    '2021-03-19','2021-03-21','2021-03-24',
                    '2021-03-27','2021-03-30','2021-04-02',
                    '2021-04-05','2021-04-08','2021-04-11',
                    '2021-04-14','2021-04-17','2021-04-20'])