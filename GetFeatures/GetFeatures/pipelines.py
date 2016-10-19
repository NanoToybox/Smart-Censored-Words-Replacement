#coding=utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import urllib
from pyltp import Segmentor

class GetfeaturesPipeline(object):
	def __init__(self):
		#self.file = codecs.open('test_single.txt', 'wb', encoding='utf-8')
		self.segmentor = Segmentor()

	def process_item(self, item, spider):
		self.segmentor.load('/Users/David/Applications/ltp_data/cws.model')  # 加载模型
		words = list(self.segmentor.segment(item["content"].encode("utf-8")) ) # 分词
		for word in words:
			self.file.write(word.decode("utf-8"))
			self.file.write("\n".decode("utf-8"))
		return item

	def close_spider(self, spider):
		self.segmentor.release()  # 释放模型
		self.file.close()