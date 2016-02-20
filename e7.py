# 10001st PRIME
# We need a list to store out prime numbers
# We will use this list to check a number if it is 
# prime.
primeList = [2]

treshold = 200000

numOfPrimes = 1
for i in range(3, treshold, 2):
	# Check if prime
	isPrime = True
	for prime in primeList:
		if (i % prime) == 0:
			isPrime = False
			break
	if isPrime:
		primeList.append(i)
		numOfPrimes += 1
	if numOfPrimes == 10001:
		break
	# Add to the list
print(numOfPrimes)
print(primeList[-1])
