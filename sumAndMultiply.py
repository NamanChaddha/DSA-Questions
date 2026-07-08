class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        arr=[]
        MOD=10**9+7
        ss=list(map(str,s))
        for i in range(len(queries)):
            x=0
            c=0
            a=ss[queries[i][0]:queries[i][1]+1]
            for t in a:
                if t!='0':
                    x=10*x+int(t)
                    c+=int(t)
            x=x*c
            arr.append(x%MOD)
        return arr
        
