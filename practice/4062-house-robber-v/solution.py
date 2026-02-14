class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        if len(colors) == 1:
            return nums[0]
            
        fin_sum = 0
        odd_sum = 0
        even_sum = 0
        n = len(colors)
        idx = 0
        
        for i, j in pairwise(colors):
            if i == j:
                if idx % 2 == 0:
                    even_sum += nums[idx]
                else:
                    odd_sum += nums[idx]
                    
            else:
                if idx % 2 == 0:
                    even_sum += nums[idx]
                else:
                    odd_sum += nums[idx]
                fin_sum += max(even_sum, odd_sum)
                even_sum = 0
                odd_sum = 0
                
            idx += 1

        if (n - 1) % 2 == 0:
            even_sum += nums[n - 1]
        else:
            odd_sum += nums[n - 1]
        
        return fin_sum + max(even_sum, odd_sum)
