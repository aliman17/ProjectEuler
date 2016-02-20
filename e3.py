# LARGEST PRIME NUMBER

def divide(i, n):
	while n % i == 0:
		n /= i
	return n

n = 600851475143
# Get factors of the number
i = 2
max_prime = 2
while i <= n:
	# Check if i divides n
	tmp = divide(i, n)
	if tmp < n:
		max_prime = i
		n = tmp	
	
	# Check next number
	i += 1
print(max_prime)
