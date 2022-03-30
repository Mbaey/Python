import numpy as np


class Solution:
    def countBattleships(self, board) -> int:
        board_arr = np.array(board)
        m, n = board_arr.shape
        visit = np.zeros((m, n))
        self.board = board
        self.visit = visit
        num = 0
        for i in range(m):
            for j in range(n):
                if visit[i][j] == 0 and self.board[i][j] == "X":
                    self.dfs(i, j)
                    num += 1
                    print(visit)
        # print(visit.shape)
        return num

    def dfs(self, i, j):
        self.visit[i][j] = 1
        m, n = self.visit.shape
        for ii, jj in zip([-1, 1, 0, 0], [0, 0, 1, -1]):
            # for jj in :
            new_i = i + ii
            new_j = j + jj
            if new_i < m and new_i >= 0 and new_j < n and new_j >= 0:

                if self.visit[new_i][new_j] == 0 and self.board[new_i][new_j] == "X":
                    self.dfs(new_i, new_j)

                self.visit[new_i][new_j] = 1


if __name__ == "__main__":

    solution = Solution()
    # 270
    print(solution.countBattleships(
        [["X", "."], [".", "X"]]
    )
    )
    # print(solution.visiblePoints(
    #     points=[[1, 0], [2, 1]], angle=13, location=[1, 1]))
