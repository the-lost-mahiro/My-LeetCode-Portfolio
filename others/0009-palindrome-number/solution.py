class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[-1 -i]:
                return False
        return True
