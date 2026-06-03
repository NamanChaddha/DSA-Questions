class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        d=s+s
        if len(s)==len(goal):
            if goal in d:
                return True
        return False
