import time
start_time = time.time()

def password_valid(number, care_about_groups=False):

	counter = 0
	digits = str(number)
	password_valid = False
	for i in range(len(digits)-1):
		if digits[i+1] == digits[i]:
			if not care_about_groups:
				password_valid = True
			counter += 1
		elif counter == 1:
			password_valid = True
			counter = 0
		else:
			counter = 0
	if counter == 1:
		password_valid = True

	return password_valid

def reset_bounds(first_password, last_password):

	for password in first_password, last_password:

		digits = [int(i) for i in str(password)]
		bound_reset = False
		for i in range(len(digits)):
			if digits[i+1] < digits[i]:
				if password == last_password:
					digits[i] -= 1
				for j in range(i+1, len(digits)):
					if password == last_password:
						digits[j] = 9
					else:
						digits[j] = digits[i]
				bound_reset = True
			if bound_reset:
				break

		new_password = int(''.join(str(i) for i in digits))
		if password == last_password:
			last_password = new_password
		else:
			first_password = new_password

	return first_password, last_password

valid_passwords = valid_passwords_no_groups = 0
first_password, last_password = reset_bounds(152085, 670283)
password = first_password
while password <= last_password:

	if password_valid(password):
		valid_passwords += 1
		if password_valid(password, care_about_groups=True):
			valid_passwords_no_groups += 1

	# Skip huge chunks of non-increasing candidate passwords
	password += 1
	digits = [int(i) for i in str(password)]
	if digits[-1] == 0:
		last_nonzero_digit = [i for i in digits if i!=0][-1]
		digits = [last_nonzero_digit if i==0 else i for i in digits]
		password = int(''.join(str(i) for i in digits))

print()
print('part 1 solution: '+ str(valid_passwords))
print('part 2 solution: '+ str(valid_passwords_no_groups))
print('total runtime: %s sec' % (time.time() - start_time))
print()
