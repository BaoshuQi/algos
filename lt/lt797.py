class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        dfs = []
        t = 0
        for i in graph:
            sorted(i)
            dfs.append((t, i))
            t += 1
        s = []
        while dfs:
            s.append(dfs.pop())
        new = [x for x in range(0, len(graph))]
        visited = []
        finished = []
        while s:
            p = s.pop()
            if p[0] in new:
                new.remove(p[0])
                visited.append(p[0])
                s.append(p)
                for n in p[1]:
                    if n in new:
                        s.append((n, graph[n]))
            elif p[0] in visited:
                visited.remove(p[0])
                finished.append(p[0])
        finished.reverse()
        dict = {}
        t = 0
        for i in finished:
            dict[t] = i
            t += 1
        start = 0
        end = len(graph) - 1

        if dict[start] > dict[end]:
            return []
        goal = dict[end]
        path = []
        node = []
        node.append([0])
        while node:
            ori = node.pop(0)
            for next in graph[ori[-1]]:
                if dict[next] < dict[end]:
                    node.append(ori + [next])
                if next == goal:
                    path.append(ori + [next])
        return path



