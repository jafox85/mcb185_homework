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
x = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal_seq = seq[0:30]
	trans_seq = seq[30:]
	s = False
	t = False
	for i in range(len(signal_seq)-8+1):
		b = signal_seq[i:i+8]
		if kd(b) >= 2.5:
			s = True
			break
	for i in range(len(trans_seq)-11+1):
		c = trans_seq[i:i+11]
		if kd(c) > 2:
			t = True
			break
	if t == True and s == True:
		print(defline)
		x += 1
print(x)
			