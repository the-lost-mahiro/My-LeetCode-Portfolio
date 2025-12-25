class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)

        nums.sort(reverse = True)
        n = len(nums)
        dis = k

        for i in range(k, n):

            if nums[i] >= nums[i - 1]:
                dis += 1

            else:
                break

        return n - dis 
