# 八皇后问题求解器

## 实现思路
使用回溯法，逐行放置皇后，通过集合记录已占用的列和对角线，避免冲突。

## 运行方式
```bash
python -c "from src.eight_queens import solve_eight_queens, print_board; solutions = solve_eight_queens(8); print(f'Found {len(solutions)} solutions'); print_board(solutions[0])"

## 测试方式
pytest tests/test_eight_queens.py -v
