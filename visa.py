#!/usr/bin/python
import sys
import getpass

input_args = sys.argv[1:]

if input_args:
	input = input_args
else:
	char_count = 1
	input = []
	while True:
		user_input = raw_input("Character position " + str(char_count) + ": ")
		if len(user_input) == 0:
			break

		input.append(int(user_input))
		char_count += 1

password_input = getpass.getpass()

output = []
for position in input:
	try:
		char = password_input[int(position) -1]
		output.append(char)
	except (IndexError):
		print 'Chars out of range. Exited'
		sys.exit()

print(', '.join(output))
