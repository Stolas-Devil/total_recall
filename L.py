import sys 
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w') 
 
a = [] 
 
def f1(x): 
    f2 = [] 
    for i in x: 
        for j in str(i): 
            if j != '-': 
                f2.append(int(j)) 
    return sum(f2) 
 
for i in range(int(input().split()[0])): 
    a.append([int(i) for i in input().split()]) 
 
a.sort(key=f1) 
 
for i in range(len(a)): 
    for j in a[i]: 
        print(j, end=' ') 
    if i != len(a) - 1: 
        print('')