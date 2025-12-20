from collections import deque

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        prefix_sum = [0] * (n + 2)
        prefix_sum[1] = 1
        
        max_q = deque() 
        min_q = deque() 
        
        left = 0 
        
        for i in range(n):
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)
            
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)
            
            while nums[max_q[0]] - nums[min_q[0]] > k:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()

            count = (prefix_sum[i+1] - prefix_sum[left]) % MOD      
            dp[i+1] = count
            prefix_sum[i+2] = (prefix_sum[i+1] + count) % MOD
            
        return dp[n]
