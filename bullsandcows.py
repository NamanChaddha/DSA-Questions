class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        s = list(secret)
        g = list(guess)
        for i in range(len(secret)):
            if s[i]==g[i]:
                bulls+=1
                s[i]='-1'
                g[i]='-2'
        for i in range(len(g)):
            if g[i] != '$' and g[i] in s:
                cows+=1
                s[s.index(g[i])] ='#'
        return str(bulls)+'A'+str(cows)+'B'
