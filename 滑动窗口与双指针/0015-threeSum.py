# 15. 三数之和
# - 难度：中等
# - 专题：双指针
# - 题目链接：https://leetcode.cn/problem-list/array/

# 思路
# 先固定第一个值，然后使用两数之和（有序）算法
# 1. 暴力：时间O(n^3)，空间O(1)
# 2. 双指针：时间O(n^2)，空间O(1))

# 代码：双指针
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 注意:输出的顺序和三元组的顺序并不重要。
        # 注意：答案中不可以包含重复的三元组。
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            # 优化
            # 因为是排序数组，所以如果前3个最小的数字加和大于0，
            # 则后续数组都大于0，不可能有答案，停止循环
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break

            # 优化
            # 因为是排序数组，所以如果当前数字和最大的2个数组加和小于0，
            # 则当前数字和中间数字都小于0，当前i循环不可能有答案，跳到下一个i
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
                
            # 处理针对i的重复
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # j右移，k左移
            j, k = i + 1, n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    # 处理针对j和k的重复
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif s > 0:
                    k -= 1
                else:  # s < 0
                    j += 1
        return ans
