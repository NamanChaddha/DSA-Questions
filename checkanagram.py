class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        dd={}
        if len(s)==len(t):
            for i in s:
                if i in d.keys():
                    d[i]+=1
                else:
                    d[i]=1
            for i in t:
                if i in dd.keys():
                    dd[i]+=1
                else:
                    dd[i]=1
            if d==dd:
                return 1==1
        return 1==0
