# -*- coding: utf-8 -*- 
# 日本語
from urllib2 import urlopen
import webapp2
import json
import os
import sys
import traceback
import com_func

#define

#
class WebhookHandler(webapp2.RequestHandler):
    def get(self):
    	self.response.headers['Content-Type'] = 'text/plain'
    	self.response.write("this is [GET] url" )

    def post(self):
    	# clsPub=com_mqttPub.mqttPubClass()
        clsFunc= com_func.funcClass()
        try:
        	text = clsFunc.get_message()
        	sDat  = "{'speech':'"+ text+ "'"
        	sDat += ",'displayText' :'"+ text+ "'"
        	sDat += "}"
        	sJs = json.dumps(sDat  )
        	dict = {'speech' : text , 'displayText' :text }
        	sDict =json.dumps(dict)
        	self.response.headers['Content-Type'] = 'application/json'
        	self.response.write( sDict )
        except:
        	print "--------------------------------------------"
        	print traceback.format_exc(sys.exc_info()[2])
        	print "--------------------------------------------"
#        sURL =mDnsName +"/tst/ghome/dat/device1.json"
#       result = json.load(urlopen(sURL))
#        text = "ok, リビングの温度は、" +str(result["temperature"])+ " 度です。"

app = webapp2.WSGIApplication([
    ('/webhook', WebhookHandler )
], debug=True)

