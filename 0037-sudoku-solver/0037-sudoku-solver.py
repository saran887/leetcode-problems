class Solution:
    def solveSudoku(self, board):
        from collections import defaultdict

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Step 1: Fill in the sets and track empty cells
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    empty.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)

        def backtrack(index):
            if index == len(empty):
                return True
            i, j = empty[index]
            box_index = (i // 3) * 3 + j // 3
            for num in '123456789':
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_index]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)

                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_index].remove(num)
            return False

        backtrack(0)
