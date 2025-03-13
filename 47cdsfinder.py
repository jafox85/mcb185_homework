import mcb185
import sys


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq)):
		f_m = seq[i:i+3]
		f_m2 = mcb185.translate(f_m)
		if f_m2 == 'M':
			protein = ['M']
			for i2 in range(i+4,len(seq),3):
				aad = seq[i2:i2+3]
				aad2 = mcb185.translate(aad)
				if aad2 == '*':
					protein.append('*')
					break
				protein.append(aad2)
			if len(protein) > 100:
				print('>' + defline)
				print(''.join(protein))
			

	