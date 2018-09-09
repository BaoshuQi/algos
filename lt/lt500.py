class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []
        for word in words:
            if all(c in list("QWERTYUIOPqwertyuiop") for c in word) or all(
                    c in list("ASDFGHJKLasdfghjkl") for c in word) or all(c in list("ZXCVBNMzxcvbnm") for c in word):
                ret.append(word)
        return ret

