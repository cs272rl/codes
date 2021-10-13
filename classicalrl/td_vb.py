# Author: Yu-Tang Shen (Fall 2020)
# model-free prediction slides - AB example

import random
vb = 0.0
b = [0, 1, 1, 1, 1, 1, 1, 0]

alpha = float(input('alpha = '))
print('alpha: {}'.format(alpha))
for _ in range(100000):
	vb = vb + alpha * (b[random.randint(0, 7)] - vb)
print(vb)
