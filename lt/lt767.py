class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import collections
        l = list(S)
        counter = collections.Counter(l).most_common()
        if counter[0][1] >= len(l) * 0.5 + 1:
            return ""
        print(counter)
        ret = [0] * len(l)
        c = 0
        for ch in counter:
            for i in range (0, ch[1]):
                ret[c] = ch[0]
                c += 2
                if c >= len(l):
                    c = 1
        return "".join(ret)

