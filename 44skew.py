import sequence
import sys
import mcb185

w = sys.argv[2]
w = int(w)
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	ini = seq[0:w]
	c = ini.count('C')
	g = ini.count('G')
	print(0, sequence.gc_comp(ini), sequence.gc_skew(ini))
	for i in range(1, len(seq) -w + 1):
		if seq[i-1] == 'C': c -= 1
		if seq[i-1] == 'G': g -= 1
		if seq[i+w-1] == 'C': c += 1
		if seq[i+w-1] == 'G': g += 1
		if g + c == 0:
			print(0)
			continue
		print(i, (c + g) / w, (g - c) / (g + c))

	