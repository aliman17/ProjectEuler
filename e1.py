# Find multiples of 3
n = 1000

sum = 0
for i in range(3, 1000, 3):
	sum += i

for i in range(5, 1000, 5):
	if i%3 != 0:
		sum += i

print(sum)

# Find multiples of 5 and check that it's not contained
# in series of 3 too. 

