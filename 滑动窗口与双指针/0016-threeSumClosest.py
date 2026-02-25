class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans_sum = nums[0] + nums[1] + nums[2]
        ans_diff = abs(ans_sum - target)
        for i in range(n-2):
            # 优化！！！
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 优化！！！
            s1 = nums[i] + nums[i+1] + nums[i+2]
            if s1 > target:
                # 后面无论怎么选，选出的三数之和不会比现在还小
                if abs(s1 - target) < ans_diff:
                    ans_sum = s1
                    ans_diff = abs(s1 - target)
                break

            # 优化！！！
            s2 = nums[i] + nums[-2] + nums[-1]
            if s2 < target:
                # 当前组合的最大三数之和小于target，那么i和-2之间的和也会小于target
                if abs(s2 - target) < ans_diff:
                    ans_sum = s2
                    ans_diff = abs(s2 - target)
                continue
            
            j = i + 1
            k = n - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                cur_diff = abs(cur_sum - target)
                if cur_sum == target:
                    ans_sum = cur_sum
                    ans_diff = 0
                    break
                # 更新答案
                if cur_diff < ans_diff:
                    ans_sum = cur_sum
                    ans_diff = cur_diff
                # 移动指针
                if cur_sum > target:
                    k -= 1
                elif cur_sum < target:
                    j += 1
        return ans_sum
