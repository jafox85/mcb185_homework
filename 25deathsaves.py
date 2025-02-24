import random
import math
def roll(n):
	fail = 0
	success = 0
	
	death = 0
	stable = 0
	revival = 0
	for i in range(n):
		success = 0
		fail = 0
		while success < 3 and fail < 3:
			d1 = random.randint(1, 20)
			if d1 == 20:
				revival += 1
				break
			if 19 >= d1 >= 10:
				success += 1
			if d1 == 1:
				fail += 2
			elif d1 <10:
				fail += 1
		if success >= 3:
				stable += 1
		if fail >= 3:
				death += 1
	return revival / n * 100, stable / n * 100, death / n * 100
print(roll(100000))