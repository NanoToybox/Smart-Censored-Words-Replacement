#coding=utf-8
import json
import codecs
import operator

word_count_dict = {}
sieve_file = codecs.open('unwanted_feature.txt', 'r', encoding='utf-8')
sieve_list = sieve_file.readlines()

#files
start_file_no = 0
end_file_no = 17
for i in range(start_file_no, end_file_no+1):
	# load json
	result_file = codecs.open('result_'+ str(i) +'.json', 'r', encoding='utf-8')
	raw_lines = result_file.readlines()
	raw_dict = json.loads(''.join(raw_lines))
	#count appearence
	for relevant_list in raw_dict.values():
		for relevant in relevant_list:
			#sieve out redundant features
			if (relevant+"\n" in sieve_list):
				continue

			count = word_count_dict.get(relevant)
			if (count == None):
				word_count_dict[relevant] = 1
			else:
				word_count_dict[relevant] += 1
	result_file.close()
	print "result_" + str(i) + " processed"

#get sorted dict
sorted_dict = sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse=True)

#save
feat_file = codecs.open('test_feature.txt', 'w', encoding='utf-8')
for feat,num in sorted_dict:
	if (num >= (end_file_no - start_file_no + 1) * 20 ):
		#feat_file.write(feat + '\t' + unicode(num) + '\n')
		feat_file.write(feat+'\n')
feat_file.close()