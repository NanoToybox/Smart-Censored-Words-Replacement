#coding=utf-8
import json
import codecs

# move words from original txt into sample files
dirty_words_file = codecs.open('before_sampling.txt', 'r', encoding='utf-8')
word = dirty_words_file.readline().rstrip(u'\n')
counter = 0
sample_counter = 0
sample = codecs.open('samples/sample_' + str(sample_counter) + ".txt", 'w', encoding='utf-8')

#take samples
while(word != u''):
	sample.write(word + u"\n")
	counter += 1
	while( counter >= 1000 ):
		sample_counter += 1
		counter = 0
		sample.close()
		sample = codecs.open('samples/sample_' + str(sample_counter) + ".txt", 'w', encoding='utf-8')
	word = dirty_words_file.readline().rstrip(u'\n')
sample.close()