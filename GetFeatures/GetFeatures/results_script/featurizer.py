#coding=utf-8
import json
import codecs
from datetime import datetime

#read result.json, featurize into vectors
print "start at " + str(datetime.now())

feat_file =  codecs.open('test_feature.txt', 'r', encoding='utf-8')
features = feat_file.readlines()

#print features[1].rstrip(u'\n')
#print features[len(features)-1].rstrip(u'\n')

start_file_no = 0
end_file_no = 17
for i in range(start_file_no, end_file_no+1):
	#load json into dict
	result_file = codecs.open('result_'+ str(i) +'.json', 'r', encoding='utf-8')
	raw_lines = result_file.readlines()
	raw_dict = json.loads(''.join(raw_lines))
	#output file
	x_file = codecs.open('feat_data/x_'+ str(i) +'.txt', 'w', encoding='utf-8')
	x_feat_file = codecs.open('feat_data/x_feat_'+ str(i) +'.txt', 'w', encoding='utf-8')

	x_dict = {}
	#featurize X
	for key, values in raw_dict.iteritems():
		feat = []
		#iterate features to construct x(i)
		for f in features:
			feat.append(1 if f.rstrip(u'\n') in values else 0)
		x_file.write(key+"\n")
		x_feat_file.write(str(feat).lstrip('[').rstrip(']')+"\n")

	print "x_" + str(i) + " processed at " + str(datetime.now())
	x_file.close()
	x_feat_file.close()
	result_file.close()

