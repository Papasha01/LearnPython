i=0
while i<100:
	if i%3==0 and i%5==0:
		print('FizzBuzz')
	else:
		if i % 3 == 0:
			print('Fizz')
		if i % 5 == 0:
			print('Buzz')
	if i%3!=0 and i%5!=0:
		print(i)
	i+=1