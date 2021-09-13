import requests
headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
url0="https://www.allsides.com/search?search=Xinjiang&item_bundle=All&sort_by=search_api_relevance"
from lxml import etree
content=requests.get(url0,headers=headers).text
content
tree=etree.HTML(content)
name0=tree.xpath("//h3//span/a/@href")
name=[]
for item in name0:
    name.append(item)
for i in range(5):
    url=url0+"&page="+str(i+1)
    content=requests.get(url,headers=headers).text
    tree=etree.HTML(content)
    name0=tree.xpath("//h3//span/a/@href")
    for item in name0:
        name.append(item)
site=[]
for i in range(len(name)):
    site.append("https://www.allsides.com"+name[i])
from bs4 import BeautifulSoup
from lxml import etree
import time
import random
title=[]
date=[]
abstract=[]
tendency=[]
source=[]
no=[]
# def timetransfer(a):
#             mondict={"January":1,"Feburary":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
#             a=a.replace(",","").split(" ")
#             datestr=str(a[2])+"-"+str(mondict[a[0]])+"-"+str(a[1].replace("th","").replace("st","").replace("nd","").replace("rd",""))
#             return datestr
for i in range(len(site)):
    print(i)
    time.sleep(random.random())
    url=site[i]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    r=requests.get(url,headers=headers)
    content=r.text
    content1=BeautifulSoup(content,'html5lib')
    try:
        #标题
        print("title")
        a1=content1.find("div",class_="article-name").text
        print(a1)
        title.append(a1)
    except:
        a1=None
        title.append("Null")
#         print('标题')

    try:
        #日期
        a2=content1.find("div",class_="article-posted-date").text.replace("Posted on AllSides","").strip()
        #a2=timetransfer(a2)
        print(a2)
        date.append(a2)
    except:
        a2=None
        date.append("Null")
#         print('日期')

    try:
        #新闻总结
        print("abstract")
        a3=content1.find("div",class_="article-description").text.replace("\n","").replace("\t","").strip()
        print(a3)
        abstract.append(a3)
    except:
        a3=None
        abstract.append("Null")
#         print("新闻总结")


    try:
        #政治倾向
        tree=etree.HTML(content)
        a4=tree.xpath("//div[@class='article-bias']/span[@class='field-content']/a/img/@alt")
        print(a4)
        tendency.append(a4[0].replace("AllSides Media Bias Rating:","").strip())
    except:
        tendency.append("Null")
        
    try:
        #来源
        print("source")
        a6=content1.find("div",class_="article-publication").text
        print(a6)
        source.append(a6)
    except:
        source.append("Null")
    no.append(i)
    
    import pandas as pd
dict0={}
dict0["title"]=title
dict0["date"]=date
dict0["abstract"]=abstract
dict0["tendency"]=tendency
dict0["source"]=source
df1=pd.DataFrame(dict0)
df1.to_excel("D:\\如果RNN会说话\\素材_02.xlsx")