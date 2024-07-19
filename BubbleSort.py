import random

# 從1-100中不重複隨機產生9組數字
A = random.sample(range(1,100),9)

print(A)

for i in range(len(A)-1,0,-1):
    for j in range(i):
        if A[j] > A[j+1]:
            #交換數字
            A[j],A[j+1] = A[j+1],A[j]
    print("氣泡排序外層迴圈執行第", 9-i,"次")

    for item in A:
        print(item,' ',end="")
    print()
