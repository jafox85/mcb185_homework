import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for _ in range(trials):
	calendar = [0] * days
	for _ in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1
		if calendar[birthday] == 2:
			matches += 1
			break
probability = matches / trials

print(f"Probability of shared birthday: {probability:.4f}")