with open('day_01.txt', 'r') as file:
	captcha = file.readline()

total_1, total_2 = 0, 0
for i in range(len(captcha)):
	if captcha[i] == captcha[(i+1) % len(captcha)]:
		total_1 += int(captcha[i])
	if captcha[i] == captcha[(i+(len(captcha)//2)) % len(captcha)]:
		total_2 += int(captcha[i])

print('part 1 captcha solution: '+ str(total_1))
print('part 2 captcha solution: '+ str(total_2))
