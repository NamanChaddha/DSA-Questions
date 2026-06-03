class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        a=[]
        for i in s:
            if i=="(":
                if c==0:
                    c+=1
                    continue
                else:
                    a.append("(")
                    c+=1
            if i==")":
                c-=1
                if c==0:
                    continue
                else:
                    a.append(")")
        return ''.join(a)
