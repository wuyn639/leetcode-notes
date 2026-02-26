# 167. 两数之和II - 输入有序数组
# - 难度：中等
# - 专题：双指针
# - 题目链接：https://leetcode.cn/problem-list/array/

# 思路
# 通过加和当前数组的minimum和maximum，每次循环可以看到O(n)的信息量，但是暴力穷举每次循环只能看到O(1)的信息量
# 1. 暴力：时间O(n^2)，空间O(1)
# 2. 双指针：时间O(n)，空间O(1)

# 代码
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: # numbers[left] + numbers[right] < target:
                left += 1
        return []
