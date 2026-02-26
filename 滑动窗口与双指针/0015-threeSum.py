# 15. 三数之和
# - 难度：中等
# - 专题：双指针
# - 题目链接：https://leetcode.cn/problem-list/array/

# 思路
# 先固定第一个值，然后使用两数之和（有序）算法
# 1. 暴力：时间O(n^3)，空间O(1)
# 2. 双指针：时间O(n^2)，空间O(1))

# 代码：反向双指针
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 注意：答案中不可以包含重复的三元组。
        # 注意：输出的顺序和三元组的顺序并不重要。
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            # 2个小优化进行提速
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
                
            # 注意这里要跳过重复！！！
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    # 注意这里要跳过重复！！！
                    # 不用break，而是增加指针！！！
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k+1] == nums[k]:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else: # nums[j] + nums[k] > target:
                    k -= 1
        return ans
