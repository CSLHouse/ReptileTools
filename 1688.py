import requests
import re
import pandas as pd
import numpy as np
from urllib.parse import  unquote, quote

def getHTMLText(url):
 
  try:
        headers = {
            'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.6, en-JM; q=0.4, en; q=0.2',
            'Cookie': 'cookie2=1e89920970371fd169a63a9d4374754d; t=61e0446ec3cc1fc8ac82e7ce462cab47; _tb_token_=55333e633be5e; __cn_logon__=false; ad_prefer="2020/03/24 22:11:25"; isg=BBYWvLWGVJvJSmA_oxNvpPhNfswYt1rx3vx314B_DfmUQ7bd6Eb4ADax2x8KcFIJ; alicnweb=touch_tb_at%3D1585058811424; cna=yTBmE0mC3GACAXbG3Ko7tdi+; l=dBL929nHQc-0w-7iBOfClurza779CIJT8kPzaNbMiICPOTCe5dtGWZ4axOTwCn1VHsKvJ3ln6AW7BxL1yynSnxv9-Zoq64CS3dC..; h_keys="%u5927%u7406%u77f3%u9910%u76d8"; ali_ab=221.216.142.167.1585058814546.2; JSESSIONID=D2B603000101C6BC4BE1C99A8C289BCF',
            'Host': 'p4psearch.1688.com',
            'Referer': 'https://p4psearch.1688.com/p4p114/p4psearch/offer2.htm?keywords=%E8%BF%9E%E8%A1%A3%E8%A3%99%E6%89%B9%E5%8F%91&cosite=baidujj&location=landing_t4&trackid=885688131303120938374316&keywordid=%7Bkeywordid%7D&format=normal&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA&p_rs=true',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
        }


        r= requests.get(url,headers=headers)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)
        return r.text
  except:
       return ""

def parsePage(ilt,html):
   try:
       plt = re.findall(r"\"amount\":[0-9]*\.?[0-9]+",html)#售价
       print("price:", plt)
       
       #tlt = re.findall(r'\"raw_title\"\:\".*?\"',html) #名字
       #sales=re.findall(r'\"view_sales\"\:\".*?\"',html) #销量

       for i in range(len(plt)):
           print(price[i])
           #sum_sales=re.search(r'\d+',eval(sales[i].split(':')[1])).group(0)
           #title = eval(tlt[i].split(':')[1])
           
           #ilt.append([price,sum_sales,title])

       #data=pd.DataFrame(ilt,columns=('售价','销量','品名'))
       #data.to_excel('1688春夏女装.xlsx')
                
   except:
       print("F")

'''
def printGoodsList(ilt):
   tplt = "{:4}\t{:8}\t{:16}\t{:32}"
   print(tplt.format("序号","价格","销量","商品名称"))
   count = 0
   for g in ilt:
       count = count +1
       print(tplt.format(count,g[0],g[1],g[2]))
'''
    

def main():
   goods = quote('春夏女装') #春夏女装 1688网址里对应的字段
   depth = 1 #要搜1688上多少页
   

   start_url = "https://p4psearch.1688.com/p4p114/p4psearch/offer2.htm?keywords="+ goods+'&cosite=baidujj&location=landing_t4&trackid=885688131303120938374316&keywordid=%7Bkeywordid%7D&format=normal&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA&p_rs=true'
   infoList = []
   for i in range(depth):
       try:
        #    url = "https://p4psearch.1688.com/p4p114/p4psearch/offer2.htm?keywords=%E6%98%A5%E5%A4%8F%E5%A5%B3%E8%A3%85&cosite=baidujj&location=landing_t4&trackid=885688131303120938374316&keywordid=%7Bkeywordid%7D&format=normal&sortType=&descendOrder=&province=&city=&priceStart=&priceEnd=&dis=&provinceValue=%E6%89%80%E5%9C%A8%E5%9C%B0%E5%8C%BA&p_rs=true"
           url = start_url
           html = getHTMLText(url)
           parsePage(infoList,html)
       except:
           continue
   #printGoodsList(infoList)  

if __name__ == "__main__":
    main()