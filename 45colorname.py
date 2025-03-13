import sys
import math
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
min_dis = 999
fp = open(colorfile)
for line in fp:
	sline = line.split()
	rgb = sline[2]
	replace_rgb = rgb.replace(',',' ')
	s_replace_rgb = replace_rgb.split()
	r = int(s_replace_rgb[0])
	g = int(s_replace_rgb[1])
	b = int(s_replace_rgb[2])
	dis = math.sqrt((R - r) ** 2 +(G - g) ** 2 + (B - b) ** 2)
	name = sline[0]
	if dis < min_dis:
		min_dis = dis
		f_name = name
print(f_name)