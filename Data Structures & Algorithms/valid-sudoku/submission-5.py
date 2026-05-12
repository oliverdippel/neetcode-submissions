class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                current_value = board[row][col]

                if current_value == ".":
                    continue
  
                box = (row // 3) * 3 + col // 3

                if (
                    current_value in row_sets[row] or 
                    current_value in col_sets[col] or
                    current_value in box_sets[box]
                ):
                    return False
                
                row_sets[row].add(current_value)
                col_sets[col].add(current_value)
                box_sets[box].add(current_value)
        
        return True