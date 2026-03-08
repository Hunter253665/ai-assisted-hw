import pytest
from src.eight_queens import solve_eight_queens

def test_n_queens_4():
    solutions = solve_eight_queens(4)
    assert len(solutions) == 2, f"Expected 2 solutions for N=4, got {len(solutions)}"

def test_n_queens_8():
    solutions = solve_eight_queens(8)
    assert len(solutions) == 92, f"Expected 92 solutions for N=8, got {len(solutions)}"

if __name__ == "__main__":
    pytest.main([__file__])
