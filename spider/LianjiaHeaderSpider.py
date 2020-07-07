import collections
import multiprocessing

import requests,lxml.html,re
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from lxml import etree
from multiprocessing.dummy import Pool

headers = {"User-Agent": UserAgent().random}
url = "https://cq.lianjia.com/ershoufang/"

response = requests.get(url, headers = headers)
html_elem = etree.HTML(response.content)
dict = {}
if response.status_code == 200:
    direct = {}
    listl = html_elem.xpath("//div[@data-role='ershoufang']/div[1]/a/@href")
    list2 = re.findall("/ershoufang/(.*?)/",str(listl))
    list3 = html_elem.xpath("//div[@data-role='ershoufang']/div[1]/a/@href")
    list4 = html_elem.xpath("//div[@data-role='ershoufang']/div[1]/a/text()")
    print(listl)
    print(list2)
    print(list4)
    for k in range(0,len(list2)):
        direct[list4[k]] = list2[k]
    for li in list2:
        response = requests.get("https://cq.lianjia.com/ershoufang/" + li, headers=headers)
        html_elem_sub = etree.HTML(response.content)
        list_sub = html_elem_sub.xpath("//div[@data-role='ershoufang']/div[2]/a/@href")
        list_sub2 = re.findall("/ershoufang/(.*?)/",str(list_sub))
        print(len(list_sub2))
        dict[li] = list_sub2

        list5 = html_elem_sub.xpath("//div[@data-role='ershoufang']/div[2]/a/text()")
        print(len(list5))
        for k in range(0,len(list5)):
            direct[list5[k]] = list_sub2[k]
    listt = []
    for li in list2:
        for i in range(0,len(dict[li])):
            listt.append(dict[li][i])
    listt = set(listt)
    listt = list(listt)
    print(listt)

    dict2 = {}
    zero = [0]*len(listt)

    for li in list2:
        liste = dict[li]
        listx = []
        for e in liste:
            for i in range(0,len(listt)):
                if e == listt[i] and zero[i] == 0:
                    zero[i] = 1
                    listx.append(e)
                    break;
        dict2[li] = listx

    print(dict)
    print(dict2)
    print(direct)
    with open("LianjiaHeader2.txt",'w') as fp:
        for li in list2:
            fp.write(li + ":")
            fp.write(str(dict[li])+ '\n\n')


    with open("LianjiaHeader3.txt", 'w') as fp:
        for li in list2:
            fp.write(li + ":")
            fp.write(str(dict2[li]) + '\n\n')


