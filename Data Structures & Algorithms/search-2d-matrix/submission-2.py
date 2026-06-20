class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bottom_row = len(matrix)-1

        left = 0
        right = len(matrix[0])-1

        while top_row < bottom_row:
            mid_row = (top_row + bottom_row) // 2
            if matrix[mid_row][left] <= target <= matrix[mid_row][right]:
                break
            elif target < matrix[mid_row][left]:
                bottom_row = mid_row - 1
            else:
                top_row = mid_row + 1
        
        row = (top_row + bottom_row) // 2

        while left <= right:
            mid = (right + left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False 




        