import collections
import time

import requests,lxml.html,re
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from lxml import etree
from multiprocessing.dummy import Pool

name = "yubei"
sname = ['yuanboyuan', 'yuanyang', 'yuelai', 'zhaomushan', 'zhongyanggongyuan']
subname = sname[0:len(sname)]

headers = {"User-Agent": UserAgent().random}
datas = list()

def mkdir(path):
    import os
    path = path.strip()  # strip方法只要含有该字符就会去除
    # 去除首尾\符号
    path = path.rstrip('\\')
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 根据需要是否显示当前程序运行文件夹
    # print("当前程序所在位置为："+os.getcwd())
    if not isExists:
        os.makedirs(path)
        print(path + '创建成功')
        return True
    else:
        print(path + '目录已存在')
        return False

def getMaxPage(url):
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        source = response.text
        soup = BeautifulSoup(source, "html.parser")
        try:
            pageData = soup.find("div", class_ = "page-box house-lst-page-box")["page-data"]
        except:
            return 0
        # pageData = '{"totalPage":100,"curPage":1}'，通过eval()函数把字符串转换为字典
        maxPage = eval(pageData)["totalPage"]
        return  maxPage
    else:
        print("Fail status: {}".format(response.status_code))
        return None

def parsePagePer(total):
    return parsePage(total[0], total[1])

def parsePage(url, num,j):
    maxPage = getMaxPage(url)
    #  解析每个page，获取每个二手房的链接
    for pageNum in range(1, maxPage+1):
        url = "https://cq.lianjia.com/chengjiao/{}/pg{}p{}".format(subname[num],pageNum,str(j))
        print("当前正在爬取: {}".format(url))
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("div", class_ = "info")
        for i in links:
            link = i.find("a")["href"]    #每个<info clear>标签有很多<a>,而我们只需要第一个，所以用find
            detail = parseDetail(link)
            datas.append(detail)


def parseDetail(url):
    time.sleep(0.5)
    response = requests.get(url, headers = headers)
    # detail = {}
    item = {}
    item = collections.OrderedDict()
    selector = lxml.html.fromstring(response.text)
    html_elem = etree.HTML(response.content)
    with open("x.html",'w',encoding='utf-8') as fp:
        fp.write(response.text)
    if response.status_code == 200:
        try:
            item['houseNameSub'] = html_elem.xpath("/html/body/div[4]/div/h1/text()")[0]
        except:
            item['houseNameSub'] = "不存在该项"
        try:
            item['houseHref'] = url
        except:
            item['houseHref'] = "不存在该项"

        try:
            item['communityName'] = html_elem.xpath("/html/body/div[4]/div/h1/text()")[0].split()[0]
        except:
            item['communityName'] = "不存在该项"
        try:
            item['dealTime'] = html_elem.xpath("/html/body/div[4]/div/span/text()")[0]
        except:
            item['dealTime'] = "不存在该项"
        try:
            item['dealPrice'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[1]/span[1]/i/text()")[0] + '万'
        except:
            item['dealPrice'] = "不存在该项"
        try:
            item['dealUnitPrice'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[1]/b/text()")[0] + '元/平方米'
        except:
            item['dealUnitPrice'] = "不存在该项"
        try:
            item['hangoutPrice'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[1]/label/text()")[0] + '万'
        except:
            item['hangoutPrice'] = "不存在该项"

        try:
            item['dealCycle'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[2]/label/text()")[0] + '天'
        except:
            item['dealCycle'] = "不存在该项"
        try:
            item['adjustPriceTimes'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[3]/label/text()")[0] + '次'
        except:
            item['adjustPriceTimes'] = "不存在该项"
        try:
            item['visitTimes'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[4]/label/text()")[0] + '次'
        except:
            item['visitTimes'] = "不存在该项"
        try:
            item['followsNum'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[5]/label/text()")[0] + '人'
        except:
            item['followsNum'] = "不存在该项"
        try:
            item['viewNum'] = html_elem.xpath("/html/body/section[1]/div[2]/div[2]/div[3]/span[6]/label/text()")[0] + '人'
        except:
            item['viewNum'] = "不存在该项"


        try:
            item['houseModel'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[1]/div[2]/ul/li[1]/text()")[0]
        except:
            item['houseModel'] = "不存在该项"
        try:
            item['houseFloor'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[1]/div[2]/ul/li[2]/text()")[0]
        except:
            item['houseFloor'] = "不存在该项"
        try:
            item['houseArea'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[1]/div[2]/ul/li[3]/text()")[0]
        except:
            item['houseArea'] = "不存在该项"
        try:
            item['houseStructure'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[1]/div[2]/ul/li[4]/text()")[0]
        except:
            item['houseStructure'] = "不存在该项"
        try:
            item['InnerArea'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[1]/div[2]/ul/li[5]/text()")[0]
        except:
            item['InnerArea'] = "不存在该项"
        try:
            item['houseType'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[1]/div[2]/ul/li[6]/text()")[0]
        except:
            item['houseType'] = "不存在该项"
        try:
            item['houseFaced'] = html_elem.xpath("//div[@class='base']/div/ul/li[7]/text()")[0]
        except:
            item['houseFaced'] = "不存在该项"
        try:
            item['buildYear'] = html_elem.xpath("//div[@class='base']/div/ul/li[8]/text()")[0]
        except:
            item['buildYear'] = "不存在该项"
        try:
            item['decorateStatus'] = html_elem.xpath("//div[@class='base']/div/ul/li[9]/text()")[0]
        except:
            item['decorateStatus'] = "不存在该项"
        try:
            item['architectureStructure'] = html_elem.xpath("//div[@class='base']/div/ul/li[10]/text()")[0]
        except:
            item['architectureStructure'] = "不存在该项"
        try:
            item['heatedMethod'] = html_elem.xpath("//div[@class='base']/div/ul/li[11]/text()")[0]
        except:
            item['heatedMethod'] = "不存在该项"
        try:
            item['householdPer'] = html_elem.xpath("//div[@class='base']/div/ul/li[12]/text()")[0]
        except:
            item['householdPer'] = "不存在该项"
        try:
            item['hasElevator'] = html_elem.xpath("//div[@class='base']/div/ul/li[13]/text()")[0]
        except:
            item['hasElevator'] = "不存在该项"

        try:
            item['lianjiaID'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[2]/div[2]/ul/li[1]/text()")[0]
        except:
            item['lianjiaID'] = "不存在该项"
        try:
            item['dealOwner'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[2]/div[2]/ul/li[2]/text()")[0]
        except:
            item['dealOwner'] = "不存在该项"
        try:
            item['hangoutTime'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[2]/div[2]/ul/li[3]/text()")[0]
        except:
            item['hangoutTime'] = "不存在该项"
        try:
            item['houseUsage'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[2]/div[2]/ul/li[4]/text()")[0]
        except:
            item['houseUsage'] = "不存在该项"
        try:
            item['houseAgeLimit'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[2]/div[2]/ul/li[5]/text()")[0]
        except:
            item['houseAgeLimit'] = "不存在该项"
        try:
            item['houseBelong'] = html_elem.xpath("//*[@id='introduction']/div[1]/div[2]/div[2]/ul/li[6]/text()")[0]
        except:
            item['houseBelong'] = "不存在该项"
        # try:
        #     item['mortgageInfo'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[7]/span[2]/text()")[0].replace(" ","").replace( "\n", "")
        # except:
        #     item['mortgageInfo'] = "不存在该项"
        # try:
        #     item['houseCopy'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[8]/span[2]/text()")[0]
        # except:
        #     item['houseCopy'] = "不存在该项"
        try:
            item['recordDetail'] = html_elem.xpath("//*[@id='chengjiao_record']/ul/li/p/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['recordDetail'] = "不存在该项"

        try:
            item['houseLabel'] = html_elem.xpath("//div[@class='tags clear']/div[2]/a/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['houseLabel'] = "不存在该项"
        try:
            item['CoreDeal'] = html_elem.xpath("//div[@class='baseattribute clear'][1]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['CoreDeal'] = "不存在该项"
        try:
            item['neighborInfo'] = html_elem.xpath("//div[@class='baseattribute clear'][2]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['neighborInfo'] = "不存在该项"
        try:
            item['housePackage'] = html_elem.xpath("//div[@class='baseattribute clear'][3]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['housePackage'] = "不存在该项"
        try:
            item['houseTransport'] = html_elem.xpath("//div[@class='baseattribute clear'][4]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['houseTransport'] = "不存在该项"
        # try:
        #     item['communityAvePrice'] = html_elem.xpath("//*[@id='resblockCardContainer']/div/div/div[2]/div/div[1]/span/text()")[0].replace(" ", "").replace("\n", "")
        # except:
        #     item['communityAvePrice'] = "不存在该项"
        # try:
        #     item['architectureYear'] = html_elem.xpath("//*[@id='resblockCardContainer']/div/div/div[2]/div/div[2]/span/text()")[0].replace(" ", "").replace("\n", "")
        # except:
        #     item['architectureYear'] = "不存在该项"
        # try:
        #     item['architectureType'] = html_elem.xpath("//*[@id='resblockCardContainer']/div/div/div[2]/div/div[3]/span/text()")[0].replace(" ", "").replace("\n", "")
        # except:
        #     item['architectureType'] = "不存在该项"
        # try:
        #     item['bulidNums'] = html_elem.xpath("//*[@id='resblockCardContainer']/div/div/div[2]/div/div[4]/span/text()")[0].replace(" ", "").replace("\n", "")
        # except:
        #     item['bulidNums'] = "不存在该项"
        # try:
        #     item['houseNums'] = html_elem.xpath("//*[@id='resblockCardContainer']/div/div/div[2]/div/div[5]/span/text()")[0].replace(" ", "").replace("\n", "")
        # except:
        #     item['houseNums'] = "不存在该项"
        # try:
        #     item['houseNums'] = html_elem.xpath("//*[@id='resblockCardContainer']/div/div/div[2]/div/div[5]/span/text()")[0].replace(" ", "").replace("\n", "")
        # except:
        #     item['houseNums'] = "不存在该项"
        # try:
        #     item['houseSources'] = html_elem.xpath("//*[@id='resblockCardContainer']/div/div/div[2]/div/div[6]/span/a/text()")[0].replace(" ", "").replace("\n", "")
        # except:
        #     item['houseSources'] = "不存在该项"



        print(item['houseNameSub'],item['houseHref'])
        return item
    else:
        return None

if __name__ == "__main__":
    # lists = []
    # for i in range(0,len(subname)):
    #     url = "https://cq.lianjia.com/chengjiao/{}".format(subname[i])
    #     lists.append((url,i))
    # print(lists)
    #
    # with Pool(processes=1) as pool:
    #     pool.map(parsePagePer, lists)
    for i in range(0, len(subname)):
        for j in range(1,8):
            url = "https://cq.lianjia.com/chengjiao/{}/p{}".format(subname[i],str(j))
            parsePage(url,i,j)
            
        #  将所有爬取的二手房数据存储到csv, xlsx文件中
        data = pd.DataFrame(datas)
        mkdir(".\data\saled\{}".format(name))
        data.to_csv(".\data\saled\{}\lianjia_saled_{}_{}.csv".format(name,name,subname[i]), encoding='utf_8_sig', index=False)
        data.to_excel(".\data\saled\{}\lianjia_saled_{}_{}.xlsx".format(name,name,subname[i]))
        print("lianjia_{}_{}文件已写入".format(name,subname[i]))
        datas = list()
