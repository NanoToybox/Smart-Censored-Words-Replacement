#coding=utf-8
import json
import codecs
import urllib
import json
from pyltp import Segmentor

class GetfeaturesPipeline(object):
	#items refed to print statics in close_spider
	items = {}

	def __init__(self):
		self.file = codecs.open('test_multi.json', 'w', encoding='utf-8')
		self.segmentor = Segmentor()
		self.segmentor.load('/Users/David/Applications/ltp_data/cws.model')  # 加载模型

	def process_item(self, item, spider):
		counter = 0
		#segmenting content of the item
		item["content"] = list(self.segmentor.segment(item["content"].encode("utf-8")) ) # 分词
		item["counter"] = len(item["content"])
		#construct item dict
		self.items[item["key"]] = item["content"]
		return item

	def close_spider(self, spider):
		#dump json file
		self.file.write(unicode(json.dumps(self.items,  ensure_ascii= False, encoding="utf-8"), "utf-8"))
		#print static, 52 means no result due to laws
		for k,v in self.items.iteritems():
			print(str(len(v))+ "\t" + k)
		
		self.segmentor.release()  # 释放模型
		self.file.close()