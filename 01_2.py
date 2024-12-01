left = []
r = {}

def appendD(d, val):
	if d.get(val) is None:
		d[val] = 1
	else:
		d[val] += 1

with open("input.txt") as f:
	for line in f.readlines():
		fmtdln = line.strip().split()
		left.append(int(fmtdln[0]))
		appendD(r,int(fmtdln[1]))

tally = 0
for n in left:
	if r.get(n) is not None:
		tally += n*r[n]

print(tally)
