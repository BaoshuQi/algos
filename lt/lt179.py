class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        dict = {}
        for n in nums:
            f = str(n)[0]
            if f in dict:
                dict[f].append(n)
            else:
                dict[f] = [n]
        for key in dict:
            m = len(str(max(dict[key])))
            l = []
            for n in dict[key]:
                l.append((n, str(n) + max((m - len(str(n))) * str(n)[0],(m - len(str(n))) * str(n)[-1])))
                l.sort(key = lambda t: (t[1], t[0]), reverse = True)
            l = list(map(lambda t: str(t[0]), l))
            t = "".join(l)
            dict[key] = t
        s = ""
        for k in range(9, 0, -1):
            if str(k) in dict:
                s += dict[str(k)]
        if s and s[0]== '0':
            return '0'
        return s
