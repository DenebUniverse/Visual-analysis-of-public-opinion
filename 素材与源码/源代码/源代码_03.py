import pandas as pd
df=pd.read_excel("D:\\如果RNN会说话\\素材_02.xlsx")
import nltk
import re 
from nltk import word_tokenize
text=re.sub(r'[^a-zA-Z0-9\s]','',string= df["abstract"][0])
text=text.lower()
df2=df[df["title"]!="Null"]
code=list(df2.iloc[:,0])
words=nltk.word_tokenize(text)
print(words)
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
filter_text = [word for word in words if word not in stopwords.words('english') ]
def set_generator(text):
    x_set=[]
    y_set=[]
    for i in range(len(text)-4):  
        x1_set=[]
        x1_set.append(text[i])
        x1_set.append(text[i+1])
        x1_set.append(text[i+3])
        x1_set.append(text[i+4])
        x_set.append(x1_set)
        y_set.append(text[i+2])
    return x_set,y_set
word_to_id={}
id_to_word={}
for word in words:
    if word not in word_to_id:
        new_id=len(word_to_id)
        word_to_id[word]=new_id
        id_to_word[new_id]=word
x,y=set_generator(filter_text)
x0=[]
y0=[]
corpus=[]
for c in code:
    text=re.sub(r'[^a-zA-Z0-9\s]','',string= df2["abstract"][c]).lower()
    words=nltk.word_tokenize(text)
    filter_text = [word for word in words if word not in stopwords.words('english') ]
    for i in filter_text:
        corpus.append(i)
    x,y=set_generator(filter_text)
    for j in range(len(x)):
        x0.append(x[j])
        y0.append(y[j])
word_to_id={}
id_to_word={}
for word in corpus:
    if word not in word_to_id:
        new_id=len(word_to_id)
        word_to_id[word]=new_id
        id_to_word[new_id]=word
def convert_one_hot(corpus, vocab_size):
    N = corpus.shape[0]
    one_hot = np.zeros((N, vocab_size), dtype=np.int32)
    for idx, word_id in enumerate(corpus):
        one_hot[idx, word_id] = 1
    return one_hot
import numpy as np
corpus0=convert_one_hot(pd.DataFrame(corpus),len(word_to_id))
def create_contexts_target(corpus,window_size):
    target=corpus[window_size:-window_size]
    contexts=[]
    for idx in range(window_size,len(corpus)-window_size):
        cs=[]
        for t in range(-window_size,window_size+1):
            if t==0:
                continue
            cs.append(corpus[idx+t])
        cs2=(cs[0]+cs[1]+cs[2]+cs[3])/6
        contexts.append(cs2)
    return np.array(contexts),np.array(target)
x,y=create_contexts_target(corpus0,2)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.1,random_state=0)
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
model = Sequential()
model.add(Dense(300, input_shape=(x_train.shape[1],)))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(y_train.shape[1]))
model.add(Activation("softmax"))

model.compile(optimizer="Nadam", loss="categorical_crossentropy", 
              metrics=["accuracy"])
history = model.fit(x_train, y_train, batch_size=20, 
                    epochs=15, verbose=2,
                    validation_data=(x_test, y_test))
W, b = model.layers[0].get_weights()
df_weight=pd.DataFrame(W)
df_weight.to_excel("D:\\如果RNN会说话\\weight.xlsx")


weight=pd.read_excel("D:\\如果RNN会说话\\weight.xlsx")
import math
from collections import Counter
tf_idf=[]
for c in code:
    text=re.sub(r'[^a-zA-Z0-9\s]','',string= df2["abstract"][c]).lower()
    words=nltk.word_tokenize(text)
    filter_text = [word for word in words if word not in stopwords.words('english') ]
    counter=Counter(filter_text)
    dict_tf={}
    dict_idf={}
    for i in list(counter.keys()):
        dict_tf[i]=counter[i]/sum(list(counter.values()))
    for i in list(counter.keys()):
        count=0
        for x in code:
            if i in nltk.word_tokenize(re.sub(r'[^a-zA-Z0-9\s]','',string= df2["abstract"][x]).lower()):
                count=count+1
        dict_idf[i]=count
    dict_tf_idf={}
    for i in list(dict_tf.keys()):
        dict_tf_idf[i]=dict_tf[i]*(len(code)/math.log((dict_idf[i]+1)))
    dict_tf_idf_0={}
    for i in list(dict_tf_idf.keys()):
        dict_tf_idf_0[i]=dict_tf_idf[i]/sum(list(dict_tf_idf.values()))
    value=0
    for i in list(dict_tf_idf_0.keys()):
        value=weight.iloc[word_to_id[i],:]*dict_tf_idf_0[i]+value
    tf_idf.append(list(value)[1:])
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans #聚类模块
import matplotlib.pyplot as plt #画图模块
from matplotlib.font_manager import FontProperties #字体模块
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
SSE = [] #误差平方和
for i in range(1,5): #k取值1~11，做kmeans聚类，看不同k值对应的簇内误差平方和
    km = KMeans(n_clusters=i) #init：初始值选择方式，可选值：'k-means++'（用均值）、'random'（随机）、an ndarray（指定一个数组），默认为'k-means++'。
    km.fit(pd.DataFrame(tf_idf))
    SSE.append(km.inertia_)  # inertia簇内误差平方和 append()在末尾添加一列
plt.plot(range(1, 5), SSE, marker='o')  # marker添加折现上数值对应点
plt.xlabel(u'聚类组数')
plt.ylabel(u'误差平方和')
plt.savefig("D:\\如果RNN会说话\\聚类参数确定.jpg")
plt.show()

kmodel = KMeans(n_clusters=3)
kmodel.fit(pd.DataFrame(tf_idf))

label = pd.Series(kmodel.labels_) #统计各个类别的数目#Series 是一维数组按列竖着排
print(label)
num = pd.Series(kmodel.labels_).value_counts() #统计各个类别内的数目
print(num)
center = pd.DataFrame(kmodel.cluster_centers_) #找出聚类中心，质心的值
print(center)
r = pd.concat([center, num], axis = 1) #横向连接(0是纵向), 得到聚类中心对应的类别下的数目
print(r)
r.columns = list(pd.DataFrame(tf_idf).columns) + [u'类别数目'] #重命名表头
print(r)

import seaborn as sns
import matplotlib.pyplot as plt
df2_source=label.value_counts()
sns.set_style("darkgrid")
bar_plot = sns.barplot(x=(df2_source.index),y=(df2_source.values),palette="muted")
plt.xticks(rotation=90)
plt.xlabel("group number")
plt.ylabel("frequency")
plt.title("news from different clusters")
plt.savefig("D:\\如果RNN会说话\\news from different clusters.jpg")
plt.show()

df2_tendency=label.value_counts()
df2_tendency.plot.pie(labeldistance=1.1,shadow=True,explode=[0.1,0.1,0.1],startangle=45)
plt.legend(loc=(1.1,0.8))
plt.title("attribution of news in different clusters")
plt.ylabel("clusters attribution")
plt.savefig("D:\\如果RNN会说话\\attribution of news in different clusters.jpg")
plt.show()

no=[]
for i in range(label.shape[0]):
    if label[i]==2:
        no.append(i) 
media=[]
for i in no:
    media.append(df2["tendency"][code[i]])
from collections import Counter
c=Counter(media)
labels=list(dict(c).keys())
X=list(dict(c).values())
fig = plt.figure()
plt.pie(X,labels=labels,autopct='%1.2f%%',shadow=True,explode=[0.1,0.1,0.1,0.1]) #画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("cluster 2")
plt.savefig("D:\\如果RNN会说话\\cluster 2.jpg")
plt.show() 

no=[]
for i in range(label.shape[0]):
    if label[i]==1:
        no.append(i)  
media=[]
for i in no:
    media.append(df2["tendency"][code[i]])
from collections import Counter
c=Counter(media)
labels=list(dict(c).keys())
X=list(dict(c).values())
fig = plt.figure()
plt.pie(X,labels=labels,autopct='%1.2f%%',shadow=True,explode=[0.1,0.1,0.1,0.1,0.1,0.1]) #画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("cluster 1")
plt.savefig("D:\\如果RNN会说话\\cluster 1.jpg")
plt.show() 

no=[]
for i in range(label.shape[0]):
    if label[i]==0:
        no.append(i)  
media=[]
for i in no:
    media.append(df2["tendency"][code[i]])
from collections import Counter
c=Counter(media)
labels=list(dict(c).keys())
X=list(dict(c).values())
fig = plt.figure()
plt.pie(X,labels=labels,autopct='%1.2f%%',shadow=True,explode=[0.1,0.1,0.1,0.1]) #画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("cluster 0")
plt.savefig("D:\\如果RNN会说话\\cluster 0.jpg")
plt.show() 

