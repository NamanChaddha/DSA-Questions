class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        if len(asteroids)==1:
            if mass>=asteroids[0]:
                return 1==1
            else:
                return 1==0
        if mass<asteroids[0]:
            return 1==0
        else:
            asteroids[0]=asteroids[0]+mass
            for i in range(1,len(asteroids)):
                if asteroids[i]<=asteroids[i-1]:
                    asteroids[i]+=asteroids[i-1]
                else:
                    return 1==0
            return 1==1
