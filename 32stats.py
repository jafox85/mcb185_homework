import sys
import math

li = []

if len(sys.argv) < 2:
	sys.exit('error, please provide at least 2 numbers')
tt = len(sys.argv[1:])
print('The number of values', tt)

mini = sys.argv[1]
maxi = sys.argv[1]
for compare in sys.argv[1:]:
	if mini > compare:
		mini = compare
	if maxi < compare:
		maxi = compare
print('The minimum is', mini)
print('The maximum is', maxi)

mean = 0
sstard = 0
for _ in sys.argv[1:]:
	mean += float(_)
	fmean = mean / len(sys.argv[1:])
	
print('The mean is',fmean)

sstard = 0
for num in sys.argv[1:]:
	sstard += (float(_) - float(fmean)) ** 2
sd = math.sqrt(sstard / tt)
print('The sd is', sd)

if tt % 2 == 0:
	median = (float(sys.argv[int(tt/2)]) + float(sys.argv[int(tt/2) + 1])) / 2
else: median = sys.argv[math.ceil(tt/2)]
print('The median is', median)

