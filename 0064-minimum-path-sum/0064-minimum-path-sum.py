class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[ [0] * (len(grid[0])) for _ in range(len(grid))] 
        
        m = len(grid[0])
        n = len(grid)

        dp[n-1][m-1] = grid[n-1][m-1]

        for i in range(n-2,-1,-1):
            dp[i][m-1] = grid[i][m-1] + dp[i+1][m-1]

        for i in range(m-2,-1,-1):
            dp[n-1][i] = grid[n-1][i] + dp[n-1][i+1]

        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                dp[i][j] = grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        
        print(dp)
        return dp[0][0]