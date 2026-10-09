class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        needed_rights = 0
        for char in s:
            if char == '(':
                if needed_rights % 2 == 1:
                    ans += 1
                    needed_rights -= 1
                needed_rights += 2
            else:
                needed_rights -= 1
                if  needed_rights < 0:
                    ans += 1
                    needed_rights += 2
        return ans + needed_rights