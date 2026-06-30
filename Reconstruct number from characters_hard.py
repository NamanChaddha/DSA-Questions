class Solution:
    def originalDigits(self, s: str) -> str:
        digits=[0]*10
        digits[0]=s.count('z')
        digits[2]=s.count('w')
        digits[4]=s.count('u')
        digits[6]=s.count('x')
        digits[8]=s.count('g')
        digits[3]=s.count('h')-digits[8]
        digits[5]=s.count('f')-digits[4]
        digits[7]=s.count('s')-digits[6]
        digits[9]=s.count('i')-digits[5]-digits[6]-digits[8]
        digits[1]=s.count('o')-digits[0]-digits[2]-digits[4]
        result = []
        for i in range(10):    
            result.append(str(i)*digits[i])
        return "".join(result)
