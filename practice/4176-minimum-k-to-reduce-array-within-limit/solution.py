class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def nonPositive(arr, k):
            target = k ** 2
            cnt = 0
            for num in arr:
                cnt += num // k
                if num % k != 0:
                    cnt += 1
                if cnt > target:
                    return False
            return cnt <= target
        l, r = 1, sum(nums)
        mini = r
        while l <= r:
            m = (l + r) // 2
            if nonPositive(nums, m):
                mini = m
                r = m - 1
            else:
                l = m + 1
        return mini
