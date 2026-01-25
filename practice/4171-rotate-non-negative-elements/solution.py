class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        idx = []
        arr = []
        
        for i, num in enumerate(nums):
            if not num < 0:
                idx.append(i)
                arr.append(num)
                
        n_arr = len(arr)
        if n_arr <= 1:
            return nums

        k %= n_arr
        arr = arr[k:] + arr[:k]
            
        for i in range(n_arr):
            nums[idx[i]] = arr[i]

        return nums
