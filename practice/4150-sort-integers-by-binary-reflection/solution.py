class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        nums2 = []
        for num in nums:
            div = []
            if num == 0:
                div = []
            else:
                while num > 0:
                    rem = num % 2
                    num = num // 2
                    div.append(rem)
            div.reverse()
            rever = 0
            for ch in range(len(div)):
                rever += div[ch] * (2 ** ch)
            nums2.append(rever)
    
        mix = sorted(zip(nums2, nums))
        nums2_s, nums_s = zip(*mix)
    
        return(list(nums_s))

