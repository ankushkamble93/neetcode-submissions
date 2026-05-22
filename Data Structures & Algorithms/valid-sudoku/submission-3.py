class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                output = board[r][c]
                if output == ".":
                    continue
                box_idx = (r//3) * 3 + (c//3)
                if (output in rows[r]) or (output in cols[c]) or (output in boxes[box_idx]):
                    return False
                rows[r].add(output)
                cols[c].add(output)
                boxes[box_idx].add(output)
        return True