import random

nums = random.sample(range(1, 100), 9)

print(nums)

for i in range(8, 0, -1):
    max = 0
    for j in range(1, i+1):
        if nums[j] > nums[max]:
            max = j
    nums[i], nums[max] = nums[max], nums[i]
    print("選擇排序的執行結果：", 9-i, "次")
    
    for item in nums:
        print(item, ' ', end="")
        
    print()
