#coding:utf-8
'''
http://www.yumingco.com/api/?domain=yumingco&suffix=com
http://www.aaw8.com/Api/DomainApi.aspx?domain=com
0 表示查询接口出错
1 表示网络异常
200 表示接口返回成功
210 表示域名可以注册
211 表示域名已经注册
212 表示域名参数传输错误
213 查询超时
'''
import pinyin
import urllib2
import io
import sys
import random


if len(sys.argv) == 1:
	print '请带上 [音节数]  [类型:font letter]  [输出html] 参数'
	exit()
	
#检测参数
if(1):
	suffix = '.com'
	url = 'http://www.aaw8.com/Api/DomainApi.aspx?domain='
	font_num = sys.argv[1]
	domain_type = 'font'
	print_html = 0
	sample = 'abcdefghigklmnopqrstuvwxyz0123456789'

	if sys.argv[2]:
		domain_type = sys.argv[2]
	if int(sys.argv[3]):
		print_html = 1
	


#拼音组件的初始化
if(1):
	py = pinyin.PinYin()
	py.load_word()
	py.load_font()

#检测程序
def domainCheckRun(files = "domain.txt"):
	handle = io.open(files,"ab")
	try:
		while 1:
			if domain_type == 'font':
				host = py.randFontPinYin(int(font_num))
			elif domain_type == 'letter':
				host = "".join(random.sample(sample, int(font_num)))
			domain = host+suffix
			resp = urllib2.urlopen(url+domain)
			result =  resp.read()
			if(print_html):
				print result
			if result.find("""{"StateID":210,""") >= 0 :
				print domain + " true success use"
				handle.write(domain+"\n")
				handle.flush()
			else :
				print domain + " false"
	finally:
		handle.close()
	

domainCheckRun()
