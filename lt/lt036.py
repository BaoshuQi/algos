class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check(l):
            s = dict(collections.Counter(filter(lambda x: x != ".", l)))
            for n in s:
                if s[n] > 1:
                    return False
            return True

        import collections
        for l in board:
            if not check(l):
                return False

        for i in range(0, 9):
            f = []
            for c in range(0, 9):
                f.append(board[c][i])
            if not check(f):
                return False

        for i in range(0, 3):
            for b in range(0, 3):
                f = []
                for r in range(0, 3):
                    for c in range(0, 3):
                        f.append(board[3 * i + r][3 * b + c])
                if not check(f):
                    return False
        return True

