class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.board = [[0] * n for _ in range(n)]
        
    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False
            if 0 <= col - row + i < self.n and self.board[i][col - row + i] == 1:
                return False
            if 0 <= col + row - i < self.n and self.board[i][col + row - i] == 1:
                return False
        return True
        
    def solve_backtracking(self, row=0):
        if row == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True
            
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_backtracking(row + 1):
                    return True
                self.board[row][col] = 0
        return False
                
    def solve_branch_and_bound(self, row=0):
        if row == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True
            
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_branch_and_bound(row + 1):
                    return True
                self.board[row][col] = 0
        return False
                
    def print_solutions(self):
        for i, solution in enumerate(self.solutions):
            print(f"Solution {i + 1}:")
            for row in solution:
                print(" ".join("Q" if cell == 1 else "-" for cell in row))
            print()


n_queens = NQueens(4)
n_queens.solve_backtracking()
n_queens.solve_branch_and_bound()
n_queens.print_solutions()

