# SPECIAL PYTHAGOREAN TRIPLET

def find():
	for a in range(0, 1000):
		for b in range(a+1, 1000):
			c = 1000 - a - b
			if a**2 + b**2 - c**2 == 0 and b<c:
				print(a,b,c)
				return a*b*c

print(find())				

