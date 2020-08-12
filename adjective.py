import sys
import re
import json


def args_dict(args):
	args_separated = re.findall('-[a-z]+ [a-z, ]*', args)
	d = {}
	for arg in args_separated:
		key_and_val = re.split(' ', arg, maxsplit=1)
		key = key_and_val[0][1:] # remove '-' from the beginning
		values_merged = key_and_val[1].rstrip()
		value_list = re.split(' *', values_merged) # ex. 'positivus  comparativus' -> ['positivus', 'comparativus']
		d[key] = value_list
	return d


args = None
command_line_args_merged = ' '.join(sys.argv[1:])
if len(command_line_args_merged) > 0:
	args = args_dict(command_line_args_merged)
print(args)

file = open('adjective.json')
adjectives_all = json.load(file)
file.close()


def remove_declensions_other_than(adj_dict, dec_list):
	adj_with_declensions_removed = {}
	for word in adj_dict.keys():
		for declension_number in adj_dict[word].keys():
			if any([x in declension_number for x in dec_list]):
				adj_with_declensions_removed[word] = adj_dict[word]

	return adj_with_declensions_removed


# def remove_grades_other_than(adj_dict, grades_list):
# 	adj_with_grades_removed = {}
# 	for word in adj_dict.keys():
# 		for declension_number in adj_dict[word].keys():
# 			for grade in adj_dict[word][declension_number].keys():
# 				if grade in grades_list:
# 					adj_with_grades_removed[]

# 	return adj_with_declensions_removed


adj_with_declensions_removed = remove_declensions_other_than(adjectives_all, dec_list=args['d'])

print(adj_with_declensions_removed.keys())