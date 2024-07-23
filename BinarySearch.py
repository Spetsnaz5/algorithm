def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# 範例使用
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"元素 {target} 位於索引 {result}")
else:
    print(f"元素 {target} 不在列表中")
