import collections
import time

import requests,lxml.html
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from lxml import etree
from multiprocessing.dummy import Pool

name = "zhongxian"
sname = ['liangping1', 'zhongxian1']
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

def parsePage(url, num, j):
    maxPage = getMaxPage(url)
    # maxPage = 1
    #  解析每个page，获取每个二手房的链接
    for pageNum in range(1, maxPage +1):
        url = "https://cq.lianjia.com/ershoufang/{}/pg{}p{}".format(subname[num],pageNum,j)
        print("当前正在爬取: {}".format(url))
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("div", class_ = "info clear")
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
    if response.status_code == 200:
        try:
            item['houseNameSub'] = html_elem.xpath("//div[@class='title']/h1/text()")[0]
        except:
            item['houseNameSub'] = "不存在该项"
        try:
            item['houseHref'] = url
        except:
            item['houseHref'] = "不存在该项"

        try:
            # item['price'] = html_elem.xpath("//div[@class='price']/span[1]/text()")[0] + "万"
            item['price'] = html_elem.xpath("/html/body/div[5]/div[2]/div[3]/span[1]/text()")[0] + "万"
        except:
            item['price'] = "不存在该项"
        try:
            # item['unitPrice'] = html_elem.xpath("//div[@class='price']/div/div[1]/span[1]/text()")[0]
            item['unitPrice'] = html_elem.xpath("/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/span[1]/text()")[0] + "元/平方米"
        except:
            item['unitPrice'] = "不存在该项"
        try:
            item['communityName'] = html_elem.xpath("//div[@class='communityName']/a[1]/text()")[0]
        except:
            item['communityName'] = "不存在该项"
        try:
            # item['areaName'] = html_elem.xpath("//div[@class='areaName']/span[2]/text()")[0]
            item['areaName'] = html_elem.xpath("/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a/text()")[0]
        except:
            item['areaName'] = "不存在该项"
        try:
            item['visitTime'] = html_elem.xpath("//div[@class='visitTime']/span[2]/text()")[0]
        except:
            item['visitTime'] = "不存在该项"

        try:
            item['houseModel'] = html_elem.xpath("//div[@class='base']/div/ul/li[1]/text()")[0]
        except:
            item['houseHref'] = "不存在该项"
        try:
            item['houseFloor'] = html_elem.xpath("//div[@class='base']/div/ul/li[2]/text()")[0]
        except:
            item['houseFloor'] = "不存在该项"
        try:
            item['houseArea'] = html_elem.xpath("//div[@class='base']/div/ul/li[3]/text()")[0]
        except:
            item['houseArea'] = "不存在该项"
        try:
            item['houseStructure'] = html_elem.xpath("//div[@class='base']/div/ul/li[4]/text()")[0]
        except:
            item['houseStructure'] = "不存在该项"
        try:
            item['InnerArea'] = html_elem.xpath("//div[@class='base']/div/ul/li[5]/text()")[0]
        except:
            item['InnerArea'] = "不存在该项"
        try:
            item['houseType'] = html_elem.xpath("//div[@class='base']/div/ul/li[6]/text()")[0]
        except:
            item['houseType'] = "不存在该项"
        try:
            item['houseFaced'] = html_elem.xpath("//div[@class='base']/div/ul/li[7]/text()")[0]
        except:
            item['houseFaced'] = "不存在该项"
        try:
            item['architectureStructure'] = html_elem.xpath("//div[@class='base']/div/ul/li[8]/text()")[0]
        except:
            item['architectureStructure'] = "不存在该项"
        try:
            item['decorateStatus'] = html_elem.xpath("//div[@class='base']/div/ul/li[9]/text()")[0]
        except:
            item['decorateStatus'] = "不存在该项"
        try:
            item['householdPer'] = html_elem.xpath("//div[@class='base']/div/ul/li[10]/text()")[0]
        except:
            item['householdPer'] = "不存在该项"
        try:
            item['hasElevator'] = html_elem.xpath("//div[@class='base']/div/ul/li[11]/text()")[0]
        except:
            item['hasElevator'] = "不存在该项"

        try:
            item['hangoutTime'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[1]/span[2]/text()")[0]
        except:
            item['hangoutTime'] = "不存在该项"
        try:
            item['dealOwner'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[2]/span[2]/text()")[0]
        except:
            item['dealOwner'] = "不存在该项"
        try:
            item['lastDeal'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[3]/span[2]/text()")[0]
        except:
            item['lastDeal'] = "不存在该项"
        try:
            item['houseUsage'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[4]/span[2]/text()")[0]
        except:
            item['houseUsage'] = "不存在该项"
        try:
            item['houseAgeLimit'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[5]/span[2]/text()")[0]
        except:
            item['houseAgeLimit'] = "不存在该项"
        try:
            item['houseBelong'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[6]/span[2]/text()")[0]
        except:
            item['houseBelong'] = "不存在该项"
        try:
            item['mortgageInfo'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[7]/span[2]/text()")[0].replace(" ","").replace( "\n", "")
        except:
            item['mortgageInfo'] = "不存在该项"
        try:
            item['houseCopy'] = html_elem.xpath("//div[@class='transaction']/div/ul/li[8]/span[2]/text()")[0]
        except:
            item['houseCopy'] = "不存在该项"

        try:
            item['houseLabel'] = html_elem.xpath("//div[@class='introContent showbasemore']/div[1]/div/a/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['houseLabel'] = "不存在该项"
        try:
            item['houseTransport'] = html_elem.xpath("//div[@class='introContent showbasemore']/div[2]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['houseTransport'] = "不存在该项"
        try:
            item['housePackage'] = html_elem.xpath("//div[@class='introContent showbasemore']/div[3]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['housePackage'] = "不存在该项"
        try:
            item['neighborInfo'] = html_elem.xpath("//div[@class='introContent showbasemore']/div[4]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['neighborInfo'] = "不存在该项"
        try:
            item['coreDeal'] = html_elem.xpath("//div[@class='introContent showbasemore']/div[5]/div[2]/text()")[0].replace(" ", "").replace("\n", "")
        except:
            item['coreDeal'] = "不存在该项"

        print(item['houseNameSub'],item['houseHref'])
        return item
    else:
        return None

if __name__ == "__main__":
    # lists = []
    # for i in range(0,len(subname)):
    #     url = "https://cq.lianjia.com/ershoufang/{}".format(subname[i])
    #     lists.append((url,i))
    # print(lists)
    #
    # with Pool(processes=1) as pool:
    #     pool.map(parsePagePer, lists)
    for i in range(0, len(subname)):
        for j in range(1,8):
            url = "https://cq.lianjia.com/ershoufang/{}/p{}".format(subname[i],str(j))
            parsePage(url,i,j)
        #  将所有爬取的二手房数据存储到csv, xlsx文件中
        data = pd.DataFrame(datas)
        mkdir(".\data\saling\{}".format(name))
        data.to_csv(".\data\saling\{}\lianjia_saling_{}_{}.csv".format(name,name,subname[i]), encoding='utf_8_sig', index=False)
        data.to_excel(".\data\saling\{}\lianjia_saling_{}_{}.xlsx".format(name,name,subname[i]))
        print("lianjia_{}_{}文件已写入".format(name,subname[i]))
        datas = list()
        

