class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[m-1][n-1]==1:
            return 0
        if obstacleGrid[0][0]==1:
            return 0
        if m ==1 and n ==1:
            return 1

        dp = [[0] * n for i in range(m)]

        for i in range(n-2,-1,-1):
            if obstacleGrid[m-1][i]==1:
                break
            dp[m-1][i] = 1

        for i in range(m-2,-1,-1):
            if obstacleGrid[i][n-1]==1:
                break
            dp[i][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j]==1:
                    continue
                else:
                    dp[i][j]= dp[i][j+1]+dp[i+1][j]
        print(dp)
        return dp[0][0]