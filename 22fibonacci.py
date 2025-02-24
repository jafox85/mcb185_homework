import math
def Fs(n):
	rx1 = 0
	rx2 = 1
	print(rx1)
	for i in range(0, n - 1):
		next_number= rx1 + rx2
		rx1 = rx2
		rx2 = next_number
		print(rx1)
Fs(10)