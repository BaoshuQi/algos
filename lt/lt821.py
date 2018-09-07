class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        str = list()
        cnt = list()
        s = ''
        count = 0
        start = True
        for c in S:
            if c == C:
                count += 1

                if s:
                    str.append(s)
                    s = ''
            else:
                s += c
                if not(count == 0 and not start):

                    cnt.append(count)
                    start = False
                count = 0
        str.append(s)
        if s:
            str.append('')
        cnt.append(count)

        dislist = list()
        for s in range(0, len(str)):
            dis = list()

            if s == 0 and cnt[s] == 0:
                d = len(str[0]) + 1
            else:
                d = 0
            for i in range(0, len(str[s])):
                print(s)
                if s == 0 and cnt[0] == 0:
                    d -= 1
                elif i < len(str[s]) / 2 or (s == len(str) -2 and cnt[-1] == 0):
                    d += 1
                elif i > len(str[s]) / 2:
                    d -= 1
                dis.append(d)
            dislist.append(dis)
        ret = list()
        print(len(str),len(cnt))
        print(str, cnt)
        for i in range(0, len(cnt)):
            ret += [0] * cnt[i]
            ret += dislist[i]
        print(ret)
        return ret

s = Solution()
s.shortestToChar("abaa", 'b')