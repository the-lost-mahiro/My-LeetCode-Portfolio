class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        
        cur_max = nums[0]
        dele = 0
        for i, num in enumerate(nums):
            if i + 1 > k:
                if num != cur_max:
                    break
                    
            cur_max = num
            dele += 1

        return n - dele if k else n
