import math
s = 'hello world'
print(s)
###
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
print('hey "dude" don\'t tell me what to do')
###
print(s.upper())
print(s)
###
print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))
###
print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify
######
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])


for nt in seq:
	print(nt,end='')
print()

for i in range(len(seq)):
    print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s, s[::], s[::1], s[::-1])
# dna
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)
    
# tuple
tax = ('Homo', 'spaniens', 9606)
print(tax)

print(tax[0])
print(tax[::-1])

# enumerate
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)
	
cool = ('happy','sad','good','yes')
for i, coo in enumerate(cool):
	print(i, coo)

# zip()
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name, coo) in enumerate(zip(nts, names, cool)):
	print(i, nt, name, coo)

# lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop(2)
print(last)
last = nts.pop()
print(last)

nts = ['A', 'T', 'C', 'G']
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

iou = nts.copy()
iou.append('c')
iou.sort()
print(nts, iou)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

#split and join
text = 'good day     to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s= ' '.join(aas)
print(s)

#searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))

print('find G?', alph.find('G'))
print('fing Z?', alph.find('Z'))

# don't put this in your 30demo.py, it's just an example
# if thing in list: idx = list.index(thing)

#practice
l= 2,3,4,5,6,7,8,4,3,2
vals = list(l)
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
print(minimum(vals))


def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
def meanval(vals):
	tt = 0
	for val in vals:
		tt += val
	return tt/ len(vals)

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.2, 0.3, 0.4]
print(dkl(p1,p2))

import sys
print(sys.argv)

#type

i = int('42')
x = float('0.61803')
print(i * x)

print('-'.join(list('ABCDE'))[3:6])

for i in range(0, len(list)):
	for j in range(i, len(list)):
	
