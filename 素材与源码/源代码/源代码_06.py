import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import jieba

#

file_name='新疆棉'
df=pd.read_csv("D:\\如果RNN会说话\\素材_03.csv")
searchfor = ['全棉时代','￥','红豆','押题','刷题','答题','证券从业','唱吧','抽','奖','健身'
             ,'减肥','考试','房','室','厅','信用','游戏','14.9']
df = df[~df['微博正文'].str.contains('|'.join(searchfor))]

txt= "".join(i for i in df['微博正文'])

words=jieba.lcut(txt)
excludes={'##','网页','微博','链接','视频','图片','一个','这些','这个','他们','就是','因为','你们'
          ,'表示','大家','还有','一些','这么','一下','那些','这样','10','为了','对于','然后','一样'
          ,'可以','已经','时候','14.9','怎么','所以','我们'}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

file_name='新疆棉微博'
background = Image.open('D:\\如果RNN会说话\\素材_10.png')  # 作为背景轮廓图
graph = np.array(background)
wc=WordCloud(background_color="white",  # 背景颜色
            width=800,
            height=400,
            mask=graph,  # 写字用的背景图，从背景图取颜色
            max_words=300,  # 最大词语数量
            font_path="simkai.ttf",  # 字体
            max_font_size=360,  # 最大字体尺寸
            random_state=50,  # 随机角度
            scale=2,
            collocations=True,  # 避免重复单词
            )
wc.generate_from_frequencies(dict(items))  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('D:\\如果RNN会说话\\'+file_name+'WordCloud.png')  # 图片命名

file_name='HM'
df=pd.read_csv("D:\\如果RNN会说话\\素材_04.csv")
searchfor = ['全棉时代','￥','红豆','押题','刷题','答题','证券从业','唱吧','抽','奖','健身'
             ,'减肥','考试','房','室','厅','信用','游戏','14.9']
df = df[~df['微博正文'].str.contains('|'.join(searchfor))]
txt= "".join(i for i in df['微博正文'])
words=jieba.lcut(txt)
excludes={'##','网页','微博','链接','视频','图片','一个','这些','这个','他们','就是','因为','你们'
          ,'表示','大家','还有','一些','这么','一下','那些','这样','10','为了','对于','然后','一样'
          ,'可以','已经','时候','怎么','所以','我们'}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
file_name='HM微博词云'
background = Image.open('D:\\如果RNN会说话\\素材_10.png')  # 作为背景轮廓图
graph = np.array(background)
wc=WordCloud(background_color="white",  # 背景颜色
            width=800,
            height=400,
            mask=graph,  # 写字用的背景图，从背景图取颜色
            max_words=300,  # 最大词语数量
            font_path="simkai.ttf",  # 字体
            max_font_size=360,  # 最大字体尺寸
            random_state=50,  # 随机角度
            scale=2,
            collocations=True,  # 避免重复单词
            )
wc.generate_from_frequencies(dict(items))  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('D:\\如果RNN会说话\\'+file_name+'WordCloud.png')  # 图片命名

file_name='匡威'
df=pd.read_csv("D:\\如果RNN会说话\\素材_05.csv")
searchfor = ['全棉时代','￥','红豆','押题','刷题','答题','证券从业','唱吧','抽','奖','健身'
             ,'减肥','考试','房','室','厅','信用','游戏','14.9']
df = df[~df['微博正文'].str.contains('|'.join(searchfor))]
txt= "".join(i for i in df['微博正文'])

words=jieba.lcut(txt)
excludes={'##','网页','微博','链接','视频','图片','一个','这些','这个','他们','就是','因为','你们'
          ,'表示','大家','还有','一些','这么','一下','那些','这样','10','为了','对于','然后','一样'
          ,'可以','已经','时候','怎么','所以','我们'}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

file_name='匡威微博词云'
background = Image.open('D:\\如果RNN会说话\\素材_10.png')  # 作为背景轮廓图
graph = np.array(background)
wc=WordCloud(background_color="white",  # 背景颜色
            width=800,
            height=400,
            mask=graph,  # 写字用的背景图，从背景图取颜色
            max_words=300,  # 最大词语数量
            font_path="simkai.ttf",  # 字体
            max_font_size=360,  # 最大字体尺寸
            random_state=50,  # 随机角度
            scale=2,
            collocations=True,  # 避免重复单词
            )
wc.generate_from_frequencies(dict(items))  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('D:\\如果RNN会说话\\'+file_name+'WordCloud.png')  # 图片命名

file_name='阿迪达斯'
df=pd.read_csv("D:\\如果RNN会说话\\素材_06.csv")
searchfor = ['全棉时代','￥','红豆','押题','刷题','答题','证券从业','唱吧','抽','奖','健身'
             ,'减肥','考试','房','室','厅','信用','游戏','14.9']
df = df[~df['微博正文'].str.contains('|'.join(searchfor))]
txt= "".join(i for i in df['微博正文'])

words=jieba.lcut(txt)
excludes={'##','网页','微博','链接','视频','图片','一个','这些','这个','他们','就是','因为','你们'
          ,'表示','大家','还有','一些','这么','一下','那些','这样','10','为了','对于','然后','一样'
          ,'可以','已经','时候','怎么','所以','我们'}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

file_name='阿迪达斯微博词云'
background = Image.open('D:\\如果RNN会说话\\素材_10.png')  # 作为背景轮廓图
graph = np.array(background)
wc=WordCloud(background_color="white",  # 背景颜色
            width=800,
            height=400,
            mask=graph,  # 写字用的背景图，从背景图取颜色
            max_words=300,  # 最大词语数量
            font_path="simkai.ttf",  # 字体
            max_font_size=360,  # 最大字体尺寸
            random_state=50,  # 随机角度
            scale=2,
            collocations=True,  # 避免重复单词
            )
wc.generate_from_frequencies(dict(items))  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('D:\\如果RNN会说话\\'+file_name+'WordCloud.png')  # 图片命名

file_name='耐克'
df=pd.read_csv("D:\\如果RNN会说话\\素材_07.csv")
searchfor = ['全棉时代','￥','红豆','押题','刷题','答题','证券从业','唱吧','抽','奖','健身'
             ,'减肥','考试','房','室','厅','信用','游戏','14.9']
df = df[~df['微博正文'].str.contains('|'.join(searchfor))]
txt= "".join(i for i in df['微博正文'])

words=jieba.lcut(txt)
excludes={'##','网页','微博','链接','视频','图片','一个','这些','这个','他们','就是','因为','你们'
          ,'表示','大家','还有','一些','这么','一下','那些','这样','10','为了','对于','然后','一样'
          ,'可以','已经','时候','怎么','所以','我们'}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

file_name='耐克微博词云'
background = Image.open('D:\\如果RNN会说话\\素材_10.png')  # 作为背景轮廓图
graph = np.array(background)
wc=WordCloud(background_color="white",  # 背景颜色
            width=800,
            height=400,
            mask=graph,  # 写字用的背景图，从背景图取颜色
            max_words=300,  # 最大词语数量
            font_path="simkai.ttf",  # 字体
            max_font_size=360,  # 最大字体尺寸
            random_state=50,  # 随机角度
            scale=2,
            collocations=True,  # 避免重复单词
            )
wc.generate_from_frequencies(dict(items))  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('D:\\如果RNN会说话\\'+file_name+'WordCloud.png')  # 图片命名

file_name='优衣库'
df=pd.read_csv("D:\\如果RNN会说话\\素材_08.csv")
searchfor = ['全棉时代','￥','红豆','押题','刷题','答题','证券从业','唱吧','抽','奖','健身'
             ,'减肥','考试','房','室','厅','信用','游戏','14.9']
df = df[~df['微博正文'].str.contains('|'.join(searchfor))]
txt= "".join(i for i in df['微博正文'])

words=jieba.lcut(txt)
excludes={'##','网页','微博','链接','视频','图片','一个','这些','这个','他们','就是','因为','你们'
          ,'表示','大家','还有','一些','这么','一下','那些','这样','10','为了','对于','然后','一样'
          ,'可以','已经','时候','怎么','所以','我们'}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

file_name='优衣库微博词云'
background = Image.open('D:\\如果RNN会说话\\素材_10.png')  # 作为背景轮廓图
graph = np.array(background)
wc=WordCloud(background_color="white",  # 背景颜色
            width=800,
            height=400,
            mask=graph,  # 写字用的背景图，从背景图取颜色
            max_words=300,  # 最大词语数量
            font_path="simkai.ttf",  # 字体
            max_font_size=360,  # 最大字体尺寸
            random_state=50,  # 随机角度
            scale=2,
            collocations=True,  # 避免重复单词
            )
wc.generate_from_frequencies(dict(items))  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('D:\\如果RNN会说话\\'+file_name+'WordCloud.png')  # 图片命名

#noun
df = pd.read_excel('D:\\如果RNN会说话\\素材_11.xlsx')

file_name='新闻名词'
key=df.noun
value=df.frequency*400

background = Image.open('D:\\如果RNN会说话\\素材_09.png')  # 作为背景轮廓图
graph = np.array(background)
wc=WordCloud(background_color="white",  # 背景颜色
            width=200,
            height=100,
            mask=graph,  # 写字用的背景图，从背景图取颜色
#           max_words=220,  # 最大词语数量
            font_path="simkai.ttf",  # 字体
            max_font_size=600,  # 最大字体尺寸
            random_state=50,  # 随机角度
            scale=1,
            collocations=True,  # 避免重复单词
            )
for i in range(len(key)):
    key[i] = str(key[i])
dic = dict(zip(key, value))
wc.generate_from_frequencies(dic)  # 根据给定词频生成词云
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")  # 不显示坐标轴
plt.show()
wc.to_file('D:\\如果RNN会说话\\'+file_name+'WordCloud.png')

