class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n= len(p)
        dp = [[False for i in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            if(p[i-1]=="*"):
                dp[0][i] = dp[0][i-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(p[j-1]==s[i-1] or p[j-1]=="."):
                    dp[i][j] = dp[i-1][j-1]
                elif(p[j-1]=="*"):
                    if(p[j-2]==s[i-1] or p[j-2]=="."):
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]