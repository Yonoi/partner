class Solution:
    def luckyNumbers (self, matrix: list) -> list:
        m, n = len(matrix), len(matrix[0])
        
        row_min = []
        for i in range(m):
            row_min.append(min(matrix[i]))
        
        col_max = []
        for j in range(n):
            col_max.append(max([row[j] for row in matrix]))
            
        return [element for element in row_min if element in col_max]
    
if __name__ == '__main__':
    s = Solution()
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(s.luckyNumbers(matrix))