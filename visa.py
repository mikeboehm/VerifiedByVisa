#!/usr/bin/python

from sys import exit

char_count = 1
user_input = '1'

# User input
input = []
while True:
	user_input = raw_input("Character position " + str(char_count) + ": ")
	if len(user_input) == 0:
		break

	input.append(int(user_input))
	char_count += 1

password_input = raw_input("Enter password: ")

output = []
for position in input:
	try:
		char = password_input[position -1]
		output.append(char)
	except (IndexError):
		print 'chars out of range'
		exit()

print(', '.join(output))
