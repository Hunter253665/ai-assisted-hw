def solve_eight_queens(n=8):
    """
    使用回溯法求解n皇后问题
    :param n: 棋盘大小，默认为8
    :return: 所有合法的解，每个解是一个列表，索引代表行，值代表列
    """
    def backtrack(row, queens, cols, diags1, diags2):
        if row == n:
            solutions.append(queens.copy())
            return
        for col in range(n):
            if col not in cols and (row - col) not in diags1 and (row + col) not in diags2:
                cols.add(col)
                diags1.add(row - col)
                diags2.add(row + col)
                queens.append(col)
                backtrack(row + 1, queens, cols, diags1, diags2)
                queens.pop()
                diags2.remove(row + col)
                diags1.remove(row - col)
                cols.remove(col)

    solutions = []
    backtrack(0, [], set(), set(), set())
    return solutions

def print_board(solution):
    """
    打印单个解对应的棋盘
    """
    n = len(solution)
    for col in solution:
        print(' '.join(['Q' if c == col else '.' for c in range(n)]))
