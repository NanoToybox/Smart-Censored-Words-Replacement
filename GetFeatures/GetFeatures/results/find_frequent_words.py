#coding=utf-8
import json
import codecs
import operator
from random import shuffle

# find k most frequent appeared words
sample_file = codecs.open('test_sample.json', 'r', encoding='utf-8')
raw_lines = sample_file.readlines()
raw_dict = json.loads(''.join(raw_lines))

word_count_dict = {}
#count appearence
for relevant_list in raw_dict.values():
	for relevant in relevant_list:
		count = word_count_dict.get(relevant)
		if (count == None):
			word_count_dict[relevant] = 1
		else:
			word_count_dict[relevant] += 1

#get sorted dict
sorted_dict = sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse=True)

#save
feat_file = codecs.open('test_feature.txt', 'w', encoding='utf-8')
for feat,num in sorted_dict:
	feat_file.write(feat + '' +  '\n') #unicode(num) +