class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            string = "1"
            
            def dem(string, count2):
                count = 1
                ans = ''
                if count2 == n:
                    return string
                else:
                    for i in range(len(string)):
                        if i == len(string) - 1:
                            ans += str(count) + string[i]

                            return dem(ans, count2 + 1)
                        else:
                            if string[i] == string[i+1]:
                                count += 1
                            else:
                                ans += str(count) + string[i]
                                count = 1
        return dem(string, 1)
