import json
import random
import sys
from shortcuts import short

args = sys.argv[1:]

file = open("relative_pronoun.json")
pronouns = json.load(file)
file.close()


def count_all_entries(d):
	cnt_temp = 0
	for genre in list(d.keys()):
		for number in list(d[genre].keys()):
			for case in list(d[genre][number].keys()):
				cnt_temp = cnt_temp + 1
	return cnt_temp


cnt = count_all_entries(pronouns)

while(len(pronouns) > 0):
	genre = random.choice(list(pronouns.keys()))
	number = random.choice(list(pronouns[genre].keys()))
	case = random.choice(list(pronouns[genre][number].keys()))

	print('{} {} {}'.format(short(genre), short(case), short(number)))
	answer = input("")
	correct_answer = pronouns[genre][number][case]

	if answer == correct_answer:
		if '--repeat' not in args:
			del pronouns[genre][number][case]
			if pronouns[genre][number] == {}:
				del pronouns[genre][number]
				if pronouns[genre] == {}:
					del pronouns[genre]
			print('correct (left {})'.format(count_all_entries(pronouns)))
		else:
			print('correct')
	else:
		print('wrong. correct answer is \'{}\''.format(correct_answer))
	print('')

print('current dict is empty')