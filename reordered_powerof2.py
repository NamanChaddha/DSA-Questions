class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(31):
            if sorted(str(1<<i))==sorted(str(n)):
                return 1==1
        return 1==0
