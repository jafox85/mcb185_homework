import math
def char_to_prob(c):
	q_score = ord(c) - 33
	if q_score < 0 or q_score > 93: return None
	return 10 ** (-q_score / 10)

def prob_to_char(p):
	if p <= 0 or p >= 1: return None
	return chr(int(-10 * math.log10(p) + 33))
	
print(char_to_prob('?'))
print(prob_to_char(00.000630957344480193))