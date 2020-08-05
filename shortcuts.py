shortcuts = {
		'indicativus': 'ind',
		'praesens': 'praes',
		'imperfectum': 'imperf',
		'perfectum': 'perf',
		'futurum I': 'fut I',
		'futurum II': 'fut II',
		'plusquamperfectum': 'plusquamperf',
		'activus': 'act',
		'passivus': 'pass',
		'singularis': 'sing',
		'pluralis': 'pl',
		'first': '1',
		'second': '2',
		'third': '3',
		'person': 'p',
		'nominativus': 'nom',
		'genetivus': 'gen',
		'dativus': 'dat',
		'accusativus': 'acc',
		'ablativus': 'abl',
		'vocativus': 'voc'
	}


def short(key):
	return shortcuts.get(key, key)