#coding=utf-8
import codecs
import json


def find_word_index(word):
	file_id = -1
	line_id = -1
	for i in range(0, 18+1):
		x_file = codecs.open('../../GetFeatures/GetFeatures/results_script/results_161113/feat_data/x_'+str(i)+'.txt', 'r', encoding='utf-8')
		words = x_file.readlines()
		if word+'\n' in words :
			line_id = words.index(word+"\n")
			file_id = i
			x_file.close()
			break
		x_file.close()

	if file_id == -1:
		print "ERROR! didn't find word : " + word  + "\n"
	return (file_id, line_id)

def find_features(features, file_id, line_id):
	result = []
	x_file = codecs.open('../../GetFeatures/GetFeatures/results_script/results_161113/feat_data/x_feat_'+str(file_id)+'.txt', 'r', encoding='utf-8')
	feat_data = x_file.readlines()
	#restore original words
	counter = 0
	for is_ture in feat_data[line_id]:
		if is_ture==u"1" and counter < len(features):
			result.append(features[counter].rstrip('\n'))
		counter += 1
	x_file.close()
	return result 


grouped_file = codecs.open('group_test.txt', 'r', encoding='utf-8')
data = json.load(grouped_file)
output_file = codecs.open('case_study_result.txt', 'w', encoding='utf-8')

cases = [u"40779.com",u"西藏3.15事件"]

feature_file = codecs.open('../../GetFeatures/GetFeatures/results_script/test_feature.txt', 'r', encoding='utf-8')
features = feature_file.readlines()

for i in range(0, len(cases)):
	(file_id, line_id) = find_word_index(cases[i])
	print str(file_id) + " " + str(line_id)
	result = find_features(features, file_id, line_id)
	output_file.write("\n" + cases[i] + " -- \n")
	for w in result:
		if (w != u'\n'):
			output_file.write(w + ", ")

grouped_file.close()
