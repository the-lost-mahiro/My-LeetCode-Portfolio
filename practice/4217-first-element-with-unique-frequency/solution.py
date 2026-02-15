class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cnt_f = Counter(cnt.values())
        for n in nums:
            if cnt_f[cnt[n]] == 1:
                return n
        return -1
