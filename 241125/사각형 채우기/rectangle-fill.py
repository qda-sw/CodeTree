MOD = 10007
def recurse(n):
    if n <= 2:
        return n
    left = recurse(n-1) if dp[n-1] == -1 else dp[n-1]
    right = recurse(n-2) if dp[n-2] == -1 else dp[n-2]
    dp[n] = (left + right)%MOD
    return dp[n]

n = int(input())
dp = [-1]*(n+1)

print(recurse(n))