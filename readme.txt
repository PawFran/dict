# random_word.py
# should be run like 'python random_word.py <dict> <start> <end>' where <dict> may be latin or eng or nothing (then latin) and start / end are number of words to include (left inclusive, right not)

# declension.py
# should be run like 'python declension.py' optionally followed by list of declensions to include ex. 'python declension.py first third mixed'
# possible: first second 'third mixed' 'third consonant' 'third vowel' 'fourth' 'fifth'

# conjugation.py
# ex. python conjugation.py -c first second -m indicativus -t praesens -v activus
# if no 'to include' is defined that all possibilities are included ex. python conjugation.py -t praesens will use all conjugations and time praesens
# right now to fully work one must set mode to 'indicativus' - because not all combinations ex. imperativus futurum I is possible

# count_words_in_dict.sh
# one argument - file name - if none then latin.txt

# find_duplicates_in_dict.sh
# one argument - file name - if none then latin.txt
