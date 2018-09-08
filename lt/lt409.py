class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(s)
        odd = False
        length = 0
        for c in cnt:
            if cnt[c] % 2 == 0:
                length += cnt[c]
            else:
                if not odd:
                    length += 1
                    odd = not odd
                length += cnt[c] - 1
        return length


s = Solution()
print(s.longestPalindrome("ab"))
