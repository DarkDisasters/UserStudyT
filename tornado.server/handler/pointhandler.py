
import tornado.web
from tornado.options import options

import pymongo
from pymongo import MongoClient

import setting

from PIL import Image
import io
import os.path

import json

import subprocess

class TestHandler(tornado.web.RequestHandler):
    def get(self, word):
        print('getsurvey handler', word);       
        self.write('ok');


class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class GetSlide(tornado.web.RequestHandler):
	def post(self):
		slide = int(self.get_argument('slideIndex'));
		slide += 1
		print('slide#=',  slide);
		print('slide', slide);
		self.write({
			'slideIndex': slide,
			})
		# self.render('slide' + slide + '.html')
