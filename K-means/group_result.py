#coding=utf-8
import codecs
import json

counter = 0;

group_file = codecs.open('group_test.txt', 'w', encoding='utf-8')

x_name_file = codecs.open('x_0.txt', 'r', encoding='utf-8')
x_name = x_name_file.readlines()

cluster_id_file =  codecs.open('out_test.txt', 'r', encoding='utf-8')
cluster_id = cluster_id_file.readlines()

cluster = {}

for line in cluster_id:
	if line[0] != '#' and counter < len(x_name):
		value = cluster.get(line.rstrip('\n'))
		if value == None :
			cluster[line.rstrip('\n')] = [x_name[counter].rstrip('\n')]
		else: 
			value.append(x_name[counter].rstrip('\n'))
		counter += 1

for k,v in cluster.iteritems():
	print len(v)
	
group_file.write(json.dumps(cluster,  ensure_ascii= False, encoding="utf-8"))

group_file.close()
x_name_file.close()
cluster_id_file.close()

