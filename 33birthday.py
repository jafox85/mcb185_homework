import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

if trials <= 0 or days <= 0 or people <= 0:
    sys.exit("error: all inputs must be positive integers.")


matches = 0
for _ in range(trials):
    birthdays = []
    for _ in range(people):
        birthday = random.randint(1, days)
        if birthday in birthdays: 
            matches += 1
            break
        else:
        	birthdays.append(birthday)
		
probability = matches / trials
print(probability)