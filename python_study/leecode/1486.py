n = 5
start = 0
nums = [0] * n
print(nums)
for i in range(0,n):
    nums[i] = start + 2 * i
print(nums)
res = start
for i in range(1,n):
    print(res)
    res = res ^ nums[i]
    
print(res)
    