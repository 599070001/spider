#coding:utf-8

import urllib2
import json

provice = [("110000","北京市"),
("120000","天津市"),
("130000","河北省"),
("140000","山西省"),
("150000","内蒙古"),
("210000","辽宁省"),
("220000","吉林省"),
("230000","黑龙江"),
("310000","上海市"),
("320000","江苏省"),
("330000","浙江省"),
("340000","安徽省"),
("350000","福建省"),
("360000","江西省"),
("370000","山东省"),
("410000","河南省"),
("420000","湖北省"),
("430000","湖南省"),
("440000","广东省"),
("450000","广西"),
("460000","海南省"),
("500000","重庆市"),
("510000","四川省"),
("520000","贵州省"),
("530000","云南省"),
("540000","西藏"),
("610000","陕西省"),
("620000","甘肃省"),
("630000","青海省"),
("640000","宁夏"),
("650000","新疆"),
("710000","香港"),
("720000","澳门"),
("730000","台湾"),
("810000","海外")]

url = "http://www.vegnet.com.cn/Market/GetMarketByAreaID?areaID="

def getCity(provice_id):
	ret_citys = []
	content = urllib2.urlopen(url+provice_id)
	citys = content.read()
	if citys:
		citys = json.loads(citys)
		if citys:
			for one in citys:
				ret_citys.append({'market_id':one['MarketID'],'name':one['Name'],'short_name':one['F4'],'image_id':one['ImageIDs'],'intro':one['Intro']})
	return ret_citys