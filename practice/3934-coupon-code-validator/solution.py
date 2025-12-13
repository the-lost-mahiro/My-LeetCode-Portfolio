class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        business = set(["grocery", "electronics", "pharmacy", "restaurant"])

        result = []
        for i in range(n):
            
            if businessLine[i] not in business or not isActive[i]:
                continue
                
            check = True
            if code[i] == "":
                check = False
            else:
                for char in code[i]:
                    if char.isnumeric() or char.isalpha() or char == "_":
                        pass
                    else:
                        check = False
                        break

            if check:
                result.append((businessLine[i], code[i]))   

        result.sort(key = lambda x: (x[0], x[1]))
        final = []
        for c in result:
            final.append(c[1])
          
        return final
