# LARGEST PRODUCT IN A GRID

with open('i11.txt') as f:
	content = f.readlines()

for i in range(len(content)):
	line = content[i]
	line = list(map(int, line.split()))
	content[i] = line

maxNum = 0

context = content

for i in range(len(context)):
	for j in range(len(context[0])):
		row = 0
		if j < 17:
			row = context[i][j]*context[i][j+1]*context[i][j+2]*context[i][j+3]
		ver = 0 
		if i < 17:
			ver = context[i][j]*context[i+1][j]*context[i+2][j]*context[i+3][j]
		diag = 0
		if i<17 and j<17:
			diag = context[i][j]*context[i+1][j+1]*context[i+2][j+2]*context[i+3][j+3]
		
		m = max(row, ver, diag)
		if m > maxNum:
			maxNum = m

print(maxNum)
