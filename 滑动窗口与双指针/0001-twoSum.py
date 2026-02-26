# 1. 两数之和
# - 难度：简单
# - 专题：哈希表
# - 题目链接：https://leetcode.cn/problem-list/array/

# 思路
# 1. 暴力：时间O(n^2)，空间O(1)
# 2. 哈希表：时间O(n)，空间O(n)

# 代码
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            if target-nums[i] in d:
                return [i, d[target-nums[i]]]
            d[nums[i]] = i
        return []
      
