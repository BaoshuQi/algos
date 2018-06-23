class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """


        dict = {}
        for acc in range(0, len(accounts)):
            for s in range(1, len(accounts[acc])):
                if accounts[acc][s] not in dict:
                    dict[accounts[acc][s]] = [acc]
                else:
                    dict[accounts[acc][s]] += [acc]
        res = []
        s = set()
        for acc in accounts:
            r = [acc[0]]
            add = set()
            sub = []
            for e in range(1, len(acc)):
                if acc[e] in s:
                    break
                sub.append(acc[e])
                add.add(acc[e])
            while sub:
                ele = sub.pop(0)
                if not ele in s:
                    s.add(ele)
                    for i in dict[ele]:
                        for em in range(1, len(accounts[i])):

                            sub.append(accounts[i][em])
                            add.add(accounts[i][em])

            if len(add) > 0:
                res.append(r + sorted(list(add)))

        return res
