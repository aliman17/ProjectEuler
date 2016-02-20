# summation of primes

numbers = [True] * 2000000

for i in range(2, len(numbers)):
	if not numbers[i]:
		pass
	else:
		for j in range(2*i, 2000000, i):
			numbers[j] = False

sum = 0
for i in range(2, 2000000):
	if numbers[i]:
		sum += i

print(sum)
	
