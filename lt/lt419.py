class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ret = 0
        init = ['.'] * (len(board[0]) + 1)
        for l in board:
            now = ['.'] + l
            for i in range(0, len(now)):
                if i > 0 and now[i - 1] != now[i] and now[i] == 'X' and now[i] != init[i]:
                        ret += 1
            init = now
        return ret









s = Solution()

print(s.countBattleships(
    [["X",".",".","X"],
     [".",".",".","X"],
     [".",".",".","X"]]))