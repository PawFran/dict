import random
import sys
import re

# todo option to skip words already asked
# take only some portion of all words (random)
# add flags for start / end
# do not use latin as default dict
# filter out lines starting with '#'

def parse_dict(lines, start=None, end=None):

	print (start)
	print(end)
	dict = {}

	current_key = None
	current_values = []

	if start == None:
		start = 1
	if end == None:
		end = len(lines) # always greater or equal # of words in dictionary

	current_element = 1
	for line in lines:
		if current_element >= start and current_element <= end:
			if not line[0].isdigit():
				current_element = current_element + 1
				dict[current_key] = current_values
				current_key = line
				current_values = []
			else:
				current_values.append(line)

	del dict[None]

	return dict

start = None
end = None
if len(sys.argv) == 1:
	file_name = 'latin.txt'
elif len(sys.argv) == 2:
	file_name = "{}.txt".format(sys.argv[1])
elif len(sys.argv) == 3:
	file_name = 'latin.txt'
	start = sys.argv[1]
	end = sys.argv[2]
else:
	file_name = "{}.txt".format(sys.argv[1])
	start = sys.argv[2]
	end = sys.argv[3]

lines_raw = open(file_name, "r").readlines()
lines = [line.strip() for line in lines_raw if len(line.rstrip()) > 0]

dict = parse_dict(lines, int(start), int(end))

while(True):
	word = random.choice(list(dict.keys()))
	base_form = word.split(' ')[0].replace(',', '')
	translation = dict[word]

	print(base_form, end=' ')
	input("")
	print(word, end=' ')
	input("")
	for line in translation:
		print(line)

	input("")
