#!/usr/bin/python3
# vim:set ts=4

from iast import iast_to_deva, deva_to_iast
from sys import argv

table = [
	['ka', 'kha', 'ga', 'gha', 'ṅa', 'ca', 'cha', 'ja', 'jha', 'ña'],
	['ṭa', 'ṭha', 'ḍa', 'ḍha', 'ṇa', 'ta', 'tha', 'da', 'dha', 'na'],
	['pa', 'pha', 'ba', 'bha', 'ma'],
	['ya', 'ra', 'la', 'va', 'śa', 'ṣa', 'sa', 'ha']
]

def compile_table(table):
	ret = {}
	for line in table:
		for i in range(len(line)):
			ret[iast_to_deva(line[i])] = (i + 1) % 10
	return ret

def is_virama(c):
	return c == 0x094d

def katapayadi(word):
	word = iast_to_deva(word)

	letters = []
	for c in word:
		if is_virama(ord(c)):
			letters.pop()
			continue
		if c in table:
			letters.append(c)

	n = ''
	for c in letters:
		x = table[c]
		n = str(x) + n

	return n

def digital_root(n):
	ret = 0
	for c in str(n):
		ret += int(c)
	while ret > 9:
		ret = digital_root(ret)
	return ret

if __name__ == '__main__':
	table = compile_table(table)
	for arg in argv[1:]:
		arg = deva_to_iast(arg)
		n = katapayadi(arg)
		print('%s = %s (→ %d)' % (arg, n, digital_root(n)))
