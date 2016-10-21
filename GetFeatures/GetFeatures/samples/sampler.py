#coding=utf-8
import codecs
from random import shuffle

# move words from original txt into sample files
dirty_words_file = codecs.open('before_sampling.txt', 'r', encoding='utf-8')
words = dirty_words_file.readlines()
shuffle(words)

counter = 0
sample_counter = 0
sample = codecs.open('sample_' + str(sample_counter) + ".txt", 'w', encoding='utf-8')

#randomly separate samples into different files
for w in words:
	sample.write(w)
	counter += 1
	if(counter >= 1000):
		sample_counter += 1
		counter = 0
		sample.close()
		sample = codecs.open('sample_' + str(sample_counter) + ".txt", 'w', encoding='utf-8')
sample.close()