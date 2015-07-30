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
import time
import io
import sys


if len(sys.argv) == 1:
	print '请带上 [音节数] 和 [延迟] 参数'
	exit()
	
#检测参数
if(1):
	suffix = '.com'
	url = 'http://www.aaw8.com/Api/DomainApi.aspx?domain='
	font_num = sys.argv[1]
	if sys.argv[2]:
		print_html = 1
	else:
		print_html = 0
	print font_num


#拼音组件的初始化
if(1):
	py = pinyin.PinYin()
	py.load_word()
	py.load_font()

#检测程序
def domainCheckRun(files = "domain.txt"):
	handle = io.open(files,"ab")
	sleep_time = float(sys.argv[2])
	print sleep_time
	try:
		while 1:
			time.sleep(sleep_time)
			domain = py.randFontPinYin(int(font_num))+suffix
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
