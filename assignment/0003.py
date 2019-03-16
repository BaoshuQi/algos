class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max = 0
        sub = list()
        for i in range(0, len(s)):
            if s[i] not in sub:
                sub.append(s[i])
                if len(sub) > max:
                    max = len(sub)
            else:
                sub = sub[sub.index(s[i]) + 1:]
                sub.append(s[i])
        return max


print(Solution.lengthOfLongestSubstring(Solution(), ''))


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max = 0
        first = 0
        last = 0
        for i in range(0, len(s)):
            if s[i] not in s[first: last]:
                last += 1
                if last - first > max:
                    max = last - first
            else:
                first += s[first: last].index(s[i]) + 1
                last += 1
        return max
