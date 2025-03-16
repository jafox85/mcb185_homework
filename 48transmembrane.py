import sys
import mcb185

code = ["I", "V", "L", "F", "C", "M", "A", "G", "T", "S", "W", "Y", "P", "H", "E", "Q", "D", "N", "K", "R"]

score = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]
    
def kd(a):
	tot = 0
	for nt in a:
		if nt in code:
			tot += score[code.index(nt)]
	return tot / len(a)

def if_transmembrane_protein(pep,w,t):
	for i in range(len(pep) -w + 1):
		seq = pep[i:i+w]
		if kd(seq) >= t: return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	n = seq[0:30]
	c = seq[30:]
	if if_transmembrane_protein(n, 8, 2.5) and if_transmembrane_protein(c, 11, 2):
		print(defline)


