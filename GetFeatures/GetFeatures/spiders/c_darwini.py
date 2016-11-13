#coding=utf-8
import scrapy
import lxml.etree
import lxml.html
import codecs
from GetFeatures.items import GetfeaturesItem

class C_Darwini(scrapy.Spider):
	name = "c_darwini"

	def start_requests(self):
		base_url = "https://cn.bing.com/search?q=" #https://www.google.com/search?q=
		urls = {}
		#reading "dirty words"
		dirty_words_file = codecs.open('GetFeatures/samples/before_sampling.txt', 'r', encoding='utf-8') 
		lines = dirty_words_file.readlines()

		#construct urls
		for word in lines:
			w = word.rstrip(u'\n').encode("utf-8")
			#if (urls.has_key(w)):
			#	print "duplicate key: " + w
			urls[w]=(base_url + w)
		dirty_words_file.close()
	
		#construct requests
		for key,url in urls.iteritems():
			request = scrapy.Request(url=url, callback=self.parse_bing)
			request.meta['key'] = key
			yield request

	def parse_bing(self, response):
		#get texts, can be refined here
		root = lxml.html.fromstring(unicode(response.body, "utf-8"))
		lxml.etree.strip_elements(root, lxml.etree.Comment, "script", "head", "style")
		#construct item
		item = GetfeaturesItem()
		item["content"] = ' '.join(i for i in root.itertext())
		item["key"] = response.meta['key']
		return item
