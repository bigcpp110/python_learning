import requests
from my_fake_useragent import UserAgent
import json
from pymongo import MongoClient
from pyquery import PyQuery as pq
import random
import time

ua=UserAgent()
headers={
	"User-Agent":ua.random()
}



client=MongoClient(host="localhost",port=27017)
collection=client["发改委"]['辽宁1']


def parse_detail(html,url):
	ret={}
	doc=pq(html)
	ret['url'] = url
	ret['title']=doc(".news-content-main h1").text()
	ret['sourceTime']=doc(".news-info").text()
	ret['content']=doc('#ContTextSize').text()
	ret['contentUrl']=doc("#ContTextSize a").attr("href")
	print(ret)
	collection.insert_one(ret)



def parse_index(html):
	doc=pq(html)
	items=doc(".mod-body2 ul li").items()
	for item in items:
		url=item('a').attr('href')
		url="http://fgw.ln.gov.cn/"+url
		response=gethtml(url)
		parse_detail(response,url)

def gethtml(url):
	response=requests.get(url,headers=headers).content.decode('gbk')
	return response


for i in range(1,21):
	url="http://fgw.ln.gov.cn/Article_Class2.asp?ClassID=3&SpecialID=0&page="+str(i)
	response=gethtml(url)
	parse_index(response)