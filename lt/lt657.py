class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        import collections
        d = collections.Counter(moves)

        v = True
        h = True

        if d["U"] and d["D"]:
            v = d["U"] == d["D"]
        elif (d["U"] and not d["D"]) or (d["D"] and not d["U"]):
            v = False

        if d["L"] and d["R"]:
            h = d["L"] == d["R"]
        elif (d["L"] and not d["R"]) or (d["R"] and not d["L"]):
            h = False

        return h and v