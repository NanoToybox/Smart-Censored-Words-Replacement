#coding=utf-8
import scrapy
import lxml.etree
import lxml.html
import codecs
from GetFeatures.items import GetfeaturesItem

#complexity depends on pv per run
class C_Darwini(scrapy.Spider):
	name = "c_darwini"

	def start_requests(self):
		base_url = "https://cn.bing.com/search?q=" #https://www.google.com/search?q=
		urls = []
		dirty_words_file = codecs.open('dirtywords_short.txt', 'r', encoding='utf-8')
		word = dirty_words_file.readline().rstrip(u'\n')
		while(word != u''):
			urls.append(base_url+word.encode("utf-8"))
			word = dirty_words_file.readline().rstrip(u'\n')
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse_bing)

	# The unicode <-> str shit below may not be needed. this all shitholes gave me a poor sleep.
	# Don't want to touch it since then.
	def parse_bing(self, response):
		root = lxml.html.fromstring(unicode(response.body, "utf-8"))
		lxml.etree.strip_elements(root, lxml.etree.Comment, "script", "head", "style")
		item = GetfeaturesItem()
		item["content"] = ' '.join(i for i in root.itertext())
		#unicode(lxml.html.tostring(root, method="text", encoding="utf-8"), "utf-8").encode("utf-8")
		return item
