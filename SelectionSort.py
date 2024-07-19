import random

#選擇排序
x = random.sample(range(1, 100), 10)

print(x)

for j in range(len(x)):
    min = j
    for i in range(len(x) - j):
        if i+j >= len(x):
            break
        if x[i+j] < x[min]:
            min = i+j
            
    tmp = x[j]
    x[j] = x[min]
    x[min] = tmp
    
print(x)
            
