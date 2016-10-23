#coding=utf-8
import json
import codecs
import urllib
from pyltp import Segmentor

class GetfeaturesPipeline(object):
	#items refed to print statics in close_spider
	items = {}
	file_no = 0
	counter = 0
	threshold = 1000

	def __init__(self):
		self.file = self.__open_file__(self.file_no);
		self.segmentor = Segmentor()
		self.segmentor.load('/Users/David/Applications/ltp_data/cws.model')  # 加载模型

	def process_item(self, item, spider):
		#segmenting content of the item
		item["content"] = list(self.segmentor.segment(item["content"].encode("utf-8")) ) # 分词
		item["counter"] = len(item["content"])
		#construct item dict
		self.items[item["key"]] = item["content"]

		self.counter += 1;
		if(self.counter >= self.threshold):
			self.file.write(unicode(json.dumps(self.items,  ensure_ascii= False, encoding="utf-8"), "utf-8"))
			self.file.close()
			self.items = {}
			self.file_no += 1
			self.counter = 0
			self.file = self.__open_file__(self.file_no);

		return item

	def close_spider(self, spider):
		#dump json file
		self.segmentor.release()  # 释放模型
		self.file.close()

	def __open_file__(self, no):
		return codecs.open('/private/var/folders/jr/dqch5q_50ysg4g9pqhpj61xc0000gn/T/Seagate Backup Plus Drive/mac_buffer/results/result_' + str(no) +'.json', 'w', encoding='utf-8') #test_sample , raw_results
