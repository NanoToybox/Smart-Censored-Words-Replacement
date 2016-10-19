#coding=utf-8
import scrapy
import lxml.etree
import lxml.html
import codecs
from GetFeatures.items import GetfeaturesItem

#complexity depends on pv per run
class C_Darwini(scrapy.Spider):
	name = "c_darwini"
	base_url = "https://cn.bing.com/search?q="

	def start_requests(self):
		#dirty_words = self.file = codecs.open('test_single.txt', 'wb', encoding='utf-8')
		urls = [
			"http://cn.bing.com/search?q=毛泽东"
		]
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
