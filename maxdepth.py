class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        max1=0
        for i in s:
            if i=='(':
                c+=1
            elif i==')':
                c-=1
            if c>max1:
                max1=c
        return max1
