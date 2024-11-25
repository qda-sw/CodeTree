

class Problem:
    def __init__(self, n):
        self.n = n
        self.dp = [0] * (n+1)
    def recurse(self, n):
        if n <= 0:
            if n == 0:
                return 1
            else:
                return 0
        if self.dp[n] != 0:
            return self.dp[n]
        self.dp[n] = (1*self.recurse(n-3) + 1*self.recurse(n-2))%10007
        return self.dp[n]
        
    def solve(self):
        return self.recurse(self.n)

n = int(input())
problem = Problem(n)
result = problem.solve()
print(result)