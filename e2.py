# FIBONACCI

a = 1
b = 2

# Create sequence
def fib(a, b):
	return (b, a+b)

sum = 0

while b <= 4000000:
	# add b into sum if applicable
	if b % 2 == 0:
		sum += b
	
	# Compute net fib. num.
	a, b = fib(a, b)

print(sum)
	


# Find a sum
