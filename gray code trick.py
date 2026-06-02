class Solution:
    def grayCode(self, n: int) -> List[int]:
        s=[]
        total=1<<n
        for i in range(total):
            s.append(i^(i>>1))
        return s
