class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left==[]:
            return n-min(right)
        elif right==[]:
            return max(left)
        else:
            return max([max(left),n-min(right)])