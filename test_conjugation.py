from conjugation import to_include

args_list = ['-c', 'first', 'second',  '-m', 'indicativus',  '-t', 'praesens',  '-v', 'activus', '--repeat']


def test_to_include():
	assert to_include('c', args_list) == ['first', 'second']
	assert to_include('m', args_list) == ['indicativus']
	assert to_include('t', args_list) == ['praesens']
	assert to_include('v', args_list) == ['activus']
	