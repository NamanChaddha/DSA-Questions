class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l=1
        ll=1
        for i in range(1,m+n-1):
            l*=i
        for j in range(1,n):
            ll*=j
        for k in range(1,m):
            ll*=k
        return l//ll
