class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        trial = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    trial.append((i,board[i][j]))
                    trial.append((board[i][j], j))
                    trial.append((i//3, j//3,board[i][j]))
        return len(trial) ==len(set(trial))