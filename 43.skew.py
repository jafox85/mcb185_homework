import sequence
seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(0, len(seq) -w +1):
	s = seq[i:i+w]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))