def equals_modulo_case_and_unicode(str1, str2):
	def replace_unicode(s):
		return s.replace('ā', 'a').replace('ē', 'e').replace('ō', 'o').replace('ū', 'u').replace('ī', 'i')
	return replace_unicode(str1.lower()) == replace_unicode(str2.lower())
	