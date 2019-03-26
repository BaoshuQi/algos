class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ret = ''
        index = 0
        if len(strs) == 0:
            return ''
        while True:
            if len(strs[0]) > index:
                s = strs[0][index]
                for st in strs:
                    if len(st) > index:
                        if s != st[index]:
                            return ret
                    else:
                        return ret
                ret += s
                index += 1
            else:
                return ret
        # return ret
