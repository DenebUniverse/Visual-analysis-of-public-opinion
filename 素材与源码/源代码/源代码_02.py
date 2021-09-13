import pandas as pd
df=pd.read_excel("D:\\如果RNN会说话\\素材_02.xlsx")
import nltk
import re 
from nltk import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
df2=df[df["title"]!="Null"]
code=list(df2.iloc[:,0])
split_words=[]
for i in code:
    text = re.sub(r'[^a-zA-Z0-9\s]','',string= df2["abstract"][i])
    words=nltk.word_tokenize(text)
    filter_text = [word for word in words if word not in stopwords.words('english') ]
    split_words.append(filter_text)
corpus=[]
for i in range(len(split_words)):
    for word in split_words[i]:
        corpus.append(word)
from collections import Counter
from nltk import pos_tag
corpus_sifted=[]
for i in code:
    text=df2["abstract"][i]
    tokens = nltk.word_tokenize(text)
    tags = pos_tag(tokens)
    for word in tags:
        if word[1]=="JJ":
            corpus_sifted.append(word[0])
        if word[1]=="RB":
            corpus_sifted.append(word[0])
        if word[1]=="RBR":
            corpus_sifted.append(word[0])
        if word[1]=="RBS":
            corpus_sifted.append(word[0])
import string
corpus_sifted2=[]
for word in corpus_sifted:
    if (word not in stop) and (word not in string.punctuation) and (word not in ["‘","’","“","”"]):
        corpus_sifted2.append(word)
a=sorted(dict(Counter(corpus_sifted2)).items(),key=lambda x:x[1],reverse=True)
adjective=[]
frequency=[]
for i in range(len(a)):
    adjective.append(a[i][0])
    frequency.append(a[i][1])
b={}
b["adjective"]=adjective
b["frequency"]=frequency
df3=pd.DataFrame(b)
df3.to_excel("D:\\如果RNN会说话\\adjectiv词频e.xlsx")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
bar_plot = sns.barplot(x=df3["adjective"][0:20],y=df3["frequency"][0:20],palette="muted")
plt.xticks(rotation=90)
plt.xlabel("adjective")
plt.ylabel("frequency")
plt.title("words frequency-adjectives")
plt.savefig("D:\\如果RNN会说话\\Adj. frequency from reports.jpg")
plt.show()

from nltk import pos_tag
corpus_sifted=[]
for i in code:
    text=df2["abstract"][i]
    tokens = nltk.word_tokenize(text)
    tags = pos_tag(tokens)
    for word in tags:
        if word[1]=="NN":
            corpus_sifted.append(word[0])
        if word[1]=="NNS":
            corpus_sifted.append(word[0])
        if word[1]=="NNP":
            corpus_sifted.append(word[0])
        if word[1]=="NNPS":
            corpus_sifted.append(word[0])
corpus_sifted2=[]
for word in corpus_sifted:
    if (word not in stop) and (word not in string.punctuation) and (word not in ["‘","’","“","”"]):
        corpus_sifted2.append(word)
corpus_sifted=[]
for i in code:
    text=df2["abstract"][i]
    tokens = nltk.word_tokenize(text)
    tags = pos_tag(tokens)
    for word in tags:
        if word[1]=="VB":
            corpus_sifted.append(word[0])
        if word[1]=="VBD" or word[1]=="VBG":
            corpus_sifted.append(word[0])
        if word[1]=="NNP":
            corpus_sifted.append(word[0])
        if word[1]=="NNPS":
            corpus_sifted.append(word[0])
corpus_sifted2=[]
for word in corpus_sifted:
    if (word not in stop) and (word not in string.punctuation) and (word not in ["‘","’","“","”"]):
        corpus_sifted2.append(word)
a=sorted(dict(Counter(corpus_sifted2)).items(),key=lambda x:x[1],reverse=True)
noun=[]
frequency=[]
for i in range(len(a)):
    noun.append(a[i][0])
    frequency.append(a[i][1])
b={}
b["noun"]=noun
b["frequency"]=frequency
df3=pd.DataFrame(b)
df3.to_excel("D:\\如果RNN会说话\\noun词频.xlsx")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
bar_plot = sns.barplot(x=df3["noun"][0:20],y=df3["frequency"][0:20],palette="muted")
plt.xticks(rotation=90)
plt.xlabel("nouns")
plt.ylabel("frequency")
plt.title("words frequency-nouns")
plt.savefig("D:\\如果RNN会说话\\N. frequency from reports.jpg")
plt.show()