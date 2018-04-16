"""recursively generate parlindrome of sub seq"""
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalin(s):
            if s == s[::-1]:
                return True
            return False

        def appendAll(s, l):
            r =  list(map(lambda rl: [s] + rl, l))
            return r
        ret = []
        if not s:
            return [[]]
        for i in range(0, len(s)):
            if isPalin(s[0:i + 1]):
                ret += appendAll(s[0:i+1], Solution.partition(self, s[i+1:]))
        return ret


print(Solution.partition(Solution(),"aab"))