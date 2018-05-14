class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        import collections
        count = collections.Counter(words).most_common()
        count.sort(key=lambda t: (-t[1], t[0]))
        l = []
        for i in range(0,k):
            l.append(count[i][0])
        return l
