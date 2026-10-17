class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // m
            col = mid - row * m

            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
        return False
