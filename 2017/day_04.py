valid_passphrases_1, valid_passphrases_2 = 0, 0
with open('day_04.txt', 'r') as potential_passphrases:
	for passphrase in potential_passphrases:
		unsorted_passphrase = passphrase.split()
		sorted_passphrase = [''.join(sorted(word)) for word in unsorted_passphrase]
		if len(unsorted_passphrase) == len(set(unsorted_passphrase)):
			valid_passphrases_1 += 1
		if len(sorted_passphrase) == len(set(sorted_passphrase)):
			valid_passphrases_2 += 1

print('valid passphrases (anagrams allowed): ' + str(valid_passphrases_1))
print('valid passphrases (anagrams disallowed): ' + str(valid_passphrases_2))