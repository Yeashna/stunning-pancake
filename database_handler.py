import os

def datafile(filename):
	lines = open(os.path.join('Database',filename)).read().splitlines()
	return set(lines)

check_sub = datafile('check_subject')
name_sub = datafile('name_subject')
help_sub = datafile('help_subject')
hello_sub = datafile('hello_subject')
