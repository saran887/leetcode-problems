class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"  

            
            found = (dfs(i+1, j, k+1) or
                     dfs(i-1, j, k+1) or
                     dfs(i, j+1, k+1) or
                     dfs(i, j-1, k+1))

            board[i][j] = temp  
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
