import random

x = random.sample(range(1, 100), 10)

print(x)

for num in range(len(x)):
    for index in range(len(x) - num):
        if index+1 >= len(x):
            break
        if x[index] > x[index+1]:
            temp = x[index + 1]
            x[index + 1] = x[index]
            x[index] = temp

print(x)
