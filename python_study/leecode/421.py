nums = [8,10,2]
if len(nums) == 1:
    print(0)
fin = 0
while len(nums) >= 1:
    i = nums[-1]
    nums.pop()
    for j in nums:
        res = i ^ j
        print(res,1)
        print(fin,1111)
        if res > fin:
            fin = res
            print(fin,2)
print("final", fin)