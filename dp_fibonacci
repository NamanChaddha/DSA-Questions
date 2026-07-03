class Solution:
    dp=[-1]*32
    dp[0]=0
    dp[1]=1
    def nthFibonacci(self, n: int) -> int:
        # code here
        
        if self.dp[n]!=-1:
            return self.dp[n]
        self.dp[n]=self.nthFibonacci(n-1)+self.nthFibonacci(n-2)
        return self.dp[n]
