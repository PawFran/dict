from declension import equals_modulo_case_and_unicode, weak_contains


def test_weak_contains():
	assert weak_contains(['third'], 'third consonant')
	assert weak_contains(['second', 'third'], 'third consonant')
	assert weak_contains(['third'], 'third')
	assert not weak_contains(['second'], 'third')
	