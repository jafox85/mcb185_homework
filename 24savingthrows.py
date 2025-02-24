import random
import math
#normal
def rolln(n):
	p1 = 0
	p2 = 0
	p3 = 0
	for i in range(n):
		pn = random.randint(1, 20)
		if pn >= 5:
			p1 += 1
		if pn >= 10:
			p2 += 1
		if pn >= 15:
			p3 += 1
	return round((p1 / n) * 100), round((p2 / n) * 100), round((p3 / n) * 100)
print(5, 10, 15)
print('normal', rolln(100000))
#advantage
def rollad(n):
	p1 = 0
	p2 = 0
	p3 = 0
	for i in range(n):
		pad_1 = random.randint(1, 20)
		pad_2 = random.randint(1, 20)
		if pad_1 >= pad_2: pad = pad_1
		else: pad = pad_2
		if pad >= 5:
				p1 += 1
		if pad >= 10:
				p2 += 1
		if pad >= 15:
				p3 += 1
	return round((p1 / n) * 100), round((p2 / n) * 100), round((p3 / n) * 100)
print('advantage', rollad(100000))
#disadvantage
def rolldis(n):
	p1 = 0
	p2 = 0
	p3 = 0
	for i in range(n):
		pad_1 = random.randint(1, 20)
		pad_2 = random.randint(1, 20)
		if pad_1 >= pad_2: pad = pad_2
		else: pad = pad_1
		if pad >= 5:
				p1 += 1
		if pad >= 10:
				p2 += 1
		if pad >= 15:
				p3 += 1
	return round((p1 / n) * 100), round((p2 / n) * 100), round((p3 / n) * 100)
print('disadvantage', rolldis(100000))