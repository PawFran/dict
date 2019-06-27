import random
import sys
import re

# todo option to skip words already asked
# take only some portion of all words (random)
# take only first or last n words
# filter out lines starting with '#'

def parse_dict(lines):
	dict = {}

	current_key = None
	current_values = []

	for line in lines:
		if not line[0].isdigit():
			dict[current_key] = current_values
			current_key = line
			current_values = []
		else:
			current_values.append(line)

	del dict[None]

	return dict


if len(sys.argv) == 1:
	file_name = 'latin.txt'
else:
	file_name = "{}.txt".format(sys.argv[1])

lines_raw = open(file_name, "r").readlines()
lines = [line.strip() for line in lines_raw if len(line.rstrip()) > 0]

dict = parse_dict(lines)

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