class Solution:
    def reverseByType(self, s: str) -> str:
        spe, spe_pos, nor, nor_pos = [], [], [], []
        
        for i, char in enumerate(s):
            
            if char.isalpha():
                nor.append(char)
                nor_pos.append(i)
                
            else:
                spe.append(char)
                spe_pos.append(i)

        spe = spe[::-1]
        nor = nor[::-1]

        i = j = pt = 0
        ans = ''

        while pt < len(s):
            
            if pt in nor_pos:
                ans += nor[i]
                i += 1

            else:
                ans += spe[j]
                j += 1

            pt += 1

        return ans
