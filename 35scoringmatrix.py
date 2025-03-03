import sys

alphabet = sys.argv[1]
match_score = int(sys.argv[2])
mismatch_score = int(sys.argv[3])

print("  ", "  ".join(alphabet))  

for base1 in alphabet:
    row = [base1]
    for base2 in alphabet:
        if base1 == base2: score = match_score
        else: score = mismatch_score
        row.append(f'{score:>2}')
    print(" ".join(row))

