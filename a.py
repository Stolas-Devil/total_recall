import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# Решение задачи

import math
a, b, c =[int(i) for i in input().split()]
h, l =[int(i) for i in input().split()]

h1 = h / 1000
l1 = l / 1000
p = l1 * h1

r = a * b

a1 = a * c
b1 = b * c
p2 = a1 * 2 + b1 * 2


p3 = p2 + r
p4 = p3 * 0.95
p5 = p4 / p

p6 = math.ceil( p5 )
print(p6)