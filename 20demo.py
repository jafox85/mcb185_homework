import math

t = 1, 2 # this is a tuple
print(t)
print(type(t))

person = 'Steven', 23, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(1,2,3,4))

mx, my = midpoint(1,2,3,4)
print(my, my)

m = midpoint(1,2,3,4)
print(m[0], m[1])

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1,10,3):
	print(i)


basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)
    
basket = 'milk', 'eggs', 'bread'
for i in range(len(basket)):
    print(basket[i])
    
for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')

# practice problems
def triangular(n):
	tri = 0
	for i in range(n+1):
		tri = tri + i
	return tri
print(triangular(4))
# factorial of number
def factorial_sum(n):
	if n == 0: return 1
	x = 1
	for i in range(1, n+1):
		x = x * i
	return x
print(factorial_sum(5))
# prob
def prob(k,n):
	p = 1
	for k in range(1, k+1):
		p = p * k
	return ((n ** k) * (math.e ** (-n))) / p
print(prob(0,1))
# n choose k
def n_k(n,k):
	return factorial_sum(n) / (factorial_sum(k) * factorial_sum(n - k))
print(n_k(1,2))
# euler 
def estimate_e(n):
	sum_e = 0
	for n in range(n):
		sum_e = sum_e + 1 / factorial_sum(n)
	return sum_e
print(estimate_e(10))
# is prime?
def prime(n):
	if n <= 1: return False
	for i in range(2, n):
		if n % i == 0: return False
	return True
print(prime(2))
# 数列
def pi(a):
	rs = 3
	for i in range(1,a+1):
		b = a * 2		
		pos = b * (b + 1) * (b + 2)
		if a % 2 == 0: rs = rs - 4 / pos
		else: rs = rs + 4 / pos
	return rs
print(pi(3))


import random

inc = 0
outc = 0
while True:
		x = (random.random())
		y = (random.random())
		z = math.sqrt(x ** 2 + y ** 2)
		if z >= 1: outc= outc + 1
		else: inc = inc + 1
		print(4 * (inc / (inc + outc)))

s = 0
i = 0
while True:
		x = (random.randint(1,6))
		y = (random.randint(1,6))
		z = (random.randint(1,6))
		i = i + 1
		s = s + x + y + z
		t = s / i
		print(t)

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
