# LARGEST PALINDROME PROCUST

# Find plindromes
polindromes = []
for i in range(100*100, 999*999+1):
	if str(i) == str(i)[::-1]:
		polindromes.append(i)

# Now we have polindromes

# Get two 3-digit factors
def factors(n):
	for i in range(100, 1000):
		if n % i == 0 and n/i < 1000:
			print(i, n/i, n)
			return True

	return False
print(polindromes)
for pol in polindromes[::-1]:
	if factors(pol):
		print(pol)
		break
		
