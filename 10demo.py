# 10demon.py by Zhitao

print ('hello,again') # greeting

"""
This is a
multi-line
comment
"""
import math
print (1.5e-2)
print (1 + 1)
print (2 - 1)
print (2 * 2)
print (1 / 3)
print (2 ** 3)
print (2 // 3)
print (5 % 2)
print(pow(2,3))
print (math.ceil(9.123))
print (math.floor(9.123))
print (math.log(3.21))
print (round(math.sqrt(5), ndigits=1))
print (math.factorial(10))
print (0.1 * 3)

a = 4
b = 2
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a),type(b),type(c),sep=',', end='!\n')

def pythagoras(a,b):
		c = math.sqrt(a**2 + b**2)
		return c

hyp = pythagoras(3,4)
print (hyp)

# function practice
def temftoc(f): return (f-32) * (5/9)

rslt1 = temftoc(45)
print (rslt1)

def gm(a,b,c): return math.pow(a*b*c,1/3)

rslt2 = gm(2,3,4)
print (rslt2)

def hm(a,b,c): return 3*(1/(1/a+1/b+1/c))

# if practice
def is_even(x):
		if x % 2 == 0: return True
		return False
print(is_even(2))
print(is_even(3))	

a=0.3
b=0.1*3
if a<b: print('a<b')
elif a>b: print('a>b')
else: print('a == b')

def silly(m, x, b):
	y = m * x + b

print(silly(2, 3, 4))

# more practice

def isinteger(a): 
		if a % 1 ==0: return True
		return False
print (isinteger(3.5))

def num(x):
		if x < 0: print(':(')
		elif x > 1: print(':(')
		else: print(':)')

num(2)

# even more practice
def max3(a,b,c):
		if a >= b and a >= c:
			return a
		elif b >= a and b >= c:
			return b
		else:
			return c

print(max3(1,2,3))
			
