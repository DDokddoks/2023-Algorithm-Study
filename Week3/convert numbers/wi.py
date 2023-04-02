def solution(x, y, n):
    dp = [9999999] * (y+1)
    dp[x] = 0
    
    for i in range(x, y+1):
        if i % 6 == 0: 
            dp[i] = min(dp[i//3]+1, dp[i//2]+1, dp[i-n]+1, dp[i])
            continue
            
        if i % 3 == 0: dp[i] = min(dp[i//3] + 1 , dp[i])
        if i % 2 == 0: dp[i] = min(dp[i//2] + 1, dp[i])
        dp[i] = min(dp[i-n]+1, dp[i])
        
    return -1 if dp[y] == 9999999 else dp[y]
