# -*- coding: utf-8 -*- 
import webapp2
import json
import os

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello world!-1017P2')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

