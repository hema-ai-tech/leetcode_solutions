class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
    
    # Convert to string and check if it reads the same forwards and backwards
        s = str(x)
        return s == s[::-1]
        if x == s:
            return "true"
        else:
            return "false"

        