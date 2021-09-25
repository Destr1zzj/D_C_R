import collections 
def deleteAndEarn(nums):
    # 创建 nums中的值出现的次数 mapping. Key 为 nums[i], value 为 nums[i] 出现的次数
    numsMap = collections.Counter(nums)
    print(numsMap)
    # nums 的最大的数字
    maxLen = max(numsMap.keys())
    print(maxLen)
    # dp 数组从 1 开始计算, 0 空出来
    dp = [0] * (maxLen + 1)
    print(dp)
    # 1 出现的次数之和
    dp[1] = 1 * numsMap[1]
    for i in range(2, maxLen + 1):
        print(dp,dp[i],dp[i-1], dp[i-2] + i * numsMap[i])
        dp[i] = max(dp[i-1], dp[i-2] + i * numsMap[i])
    print(dp[-1])

if __name__ == "__main__":

    l = [1,2,3,4,5,6,5,5,5,6]
    deleteAndEarn(l)
