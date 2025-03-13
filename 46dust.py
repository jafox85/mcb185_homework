import sys
import mcb185
import math

w = sys.argv[2]
w = int(w)
entropy_threshold = sys.argv[3]
entropy_threshold = float(entropy_threshold)

	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	newseq = list(seq)
	print(defline)
	for i in range(len(seq) - w + 1):
		window = seq[i:i+w]
		a = window.count('A')
		t = window.count('T')
		c = window.count('C')
		g = window.count('G')
		if a > 0: a_p = a / w
		else: a_p = 0
		if t > 0: t_p = t / w
		else: t_p = 0
		if c > 0: c_p = c / w
		else: c_p = 0
		if g > 0: g_p = g / w
		else: g_p = 0
		h = 0
		for p in [a_p, t_p, c_p, g_p]:
			if p > 0:
				h -= p * math.log2(p)
		if h < entropy_threshold:
			newseq[i:i+w] = ['N'] * w
	string_newseq = ''.join(newseq)
	for i in range(0,len(string_newseq),60):
		print(string_newseq[i:i+60])

