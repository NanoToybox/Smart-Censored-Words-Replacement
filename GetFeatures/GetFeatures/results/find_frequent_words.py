#coding=utf-8
import json
import codecs
import operator
from random import shuffle

# find k most frequent appeared words
sample_file = codecs.open('test_sample_0.json', 'r', encoding='utf-8')
raw_lines = sample_file.readlines()
raw_dict = json.loads(''.join(raw_lines))

#sieve: redundant features
sieve_file = codecs.open('unwanted_feature.txt', 'r', encoding='utf-8')
sieve_list = sieve_file.readlines()

word_count_dict = {}
#count appearence
for relevant_list in raw_dict.values():
	for relevant in relevant_list:
		if (relevant+"\n" in sieve_list):
			continue

		count = word_count_dict.get(relevant)
		if (count == None):
			word_count_dict[relevant] = 1
		else:
			word_count_dict[relevant] += 1

#get sorted dict
sorted_dict = sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse=True)

#save
feat_file = codecs.open('test_feature_0.txt', 'w', encoding='utf-8')
for feat,num in sorted_dict:
	feat_file.write(feat + '\t' + unicode(num) + '\n')