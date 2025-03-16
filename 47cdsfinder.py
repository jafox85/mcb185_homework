import mcb185
import sys

# 5 ATGCCCTAACAT 3
# 3 TACGGGATTGTA 5

min_length = int(sys.argv[2])

def cdsfinder(seq, min_length):
	proteins_num = 0
	for frame in range(3):
		for i in range(frame, len(seq) -3 + 1, 3):
			f_m = seq[i:i+3]
			f_m2 = mcb185.translate(f_m)
			if f_m2 == 'M':
				protein = ['M']
				for i2 in range(i+3,len(seq) -3 + 1, 3):
					aad = mcb185.translate(seq[i2:i2+3])
					if aad == '*':
						protein.append('*')
						break
					protein.append(aad)
				if len(protein) > min_length:
					print('>' + defline,' ', proteins_num)
					print(''.join(protein))
					proteins_num += 1

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	reverse = mcb185.anti_seq(seq)
	print(cdsfinder(seq, min_length))
	print(cdsfinder(reverse, min_length))