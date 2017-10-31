# -*- coding: utf-8 -*- 
# 日本語
from urllib2 import urlopen
import webapp2
import json
import os
import datetime

#define
mDnsName="http://kuc-arc-f.com"

#com_func
class funcClass:
	def __init__(self):
		print ""
	
	def get_heiNum(self, v1 ,v2):
		ret=0.0
		fv = float(v1) + float(v2)
		ret= fv / 2
		return ret
		
	def get_message(self):
		sURL =mDnsName +"/tst/ghome/dat/device5.json"
		result = json.load(urlopen(sURL))
#		text = "ok, リビングの温度は、" +str(result["temperature"])+ " 度です。"
		text = "ok, センサーをチェックします。"
		text +="リビングの温度は、" +str(result["temperature"])+ " 度です。"
		text +="湿度は、" +str(result["humidity"])+ " パーセントです。"
		text +="気圧は、" +str(result["press"])+ " ヘクトパスカルです。"
		sURL2 =mDnsName +"/tst/ghome/dat/device1.json"
		result2 = json.load(urlopen(sURL2 ))
		sBuf2 ="玄関の温度は、" + str(result2["temperature"]) +"度です。"
		text += sBuf2
		fAva= self.get_heiNum(result["temperature"] , result2["temperature"])
#		fAva= self.get_heiNum(1.0  , 2.0)
		sBuf3="室内の温度平均値は、" + str(fAva) + "度です。"
		text +=sBuf3
		#time
		tmNow = datetime.datetime.now()
		tmNow= tmNow + datetime.timedelta(hours=9)
		sHH = tmNow.strftime("%H")
		sMM = tmNow.strftime("%M")
		sTime = " 現在時刻は、" + sHH+"時"+ sMM+ "分になります。"
		text += sTime
		return text
		




