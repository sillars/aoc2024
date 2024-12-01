left = []
right = []
with open("input.txt") as f:
	for line in f.readlines():
		fmtdln = line.strip().split()
		left.append(int(fmtdln[0]))
		right.append(int(fmtdln[1]))
left = sorted(left)
right = sorted(right)

tally = 0
for i in range(len(left)):
	result = left[i] - right[i]
	tally += abs(result)

print(tally)
