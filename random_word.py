import random
import sys

# take only some portion of all words (random)
# feedback from user good/bad answer and modifying probabilities of some words based on it (difficult words more often displayed) - maybe some ml algorithm aiming at scoring points giving user words he cannot translate ?
# filter out lines starting with '#'
# only certain part of speech ex. conj
# only certain declension or conjugation
# advanced mode - one must respond to a sequence of questions: what part of speech is it and so on. but what if there's many options ?
# possibility to count how many words there are still in dictionary - ex by typing c after word


def parse_dict(lines, start, end):
    dict = {}

    current_key = None
    current_values = []

    if start is None:
        start = 1
    else:
        start = int(start)
    if end is None:
        end = len(lines)  # always greater or equal # of words in dictionary
    else:
        end = int(end)

    current_element = 1
    for line in lines:
        if start <= current_element <= end:
            if not line[0].isdigit():
                current_element = current_element + 1
                dict[current_key] = current_values
                current_key = line
                current_values = []
            else:
                current_values.append(line)
        else:
            if not line[0].isdigit():
                current_element = current_element + 1

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

dict = parse_dict(lines, start, end)

while (len(dict) > 0):
    word = random.choice(list(dict.keys()))
    base_form = word.split(' ')[0].replace(',', '')
    translation = dict[word]

    print(base_form, end=' ')
    input("")
    print(word, end=' ')
    input("")
    for line in translation:
        print(line)

    feedback = input("")
    if 'x' in feedback:
    	del dict[word]
    	print('')
    if 'c' in feedback:
    	print('there are {} words left in current dict'.format(len(dict)))
    	print('')

print('current dictionary is empty')
