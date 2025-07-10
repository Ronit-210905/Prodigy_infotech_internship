def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0  # Backtrack
                return False
    return True

def input_grid():
    print("🔢 Enter your Sudoku grid row by row:")
    print("Use 0 for empty cells.")
    grid = []
    for i in range(9):
        while True:
            row = input(f"Enter 9 digits for row {i+1} (with spaces): ")
            parts = row.strip().split()
            if len(parts) == 9 and all(p.isdigit() and 0 <= int(p) <= 9 for p in parts):
                grid.append([int(p) for p in parts])
                break
            else:
                print("❌ Invalid input. Please enter exactly 9 digits between 0–9 separated by spaces.")
    return grid

# ---- Main Program ----

sudoku_grid = input_grid()

print("\n🧩 Original Sudoku Puzzle:")
print_grid(sudoku_grid)

if solve(sudoku_grid):
    print("\n✅ Solved Sudoku Puzzle:")
    print_grid(sudoku_grid)
else:
    print("❌ No solution exists for the given puzzle.")
