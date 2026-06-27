class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        arr=[]
        x=1
        y=z
        while x<=z and y>0:
            if customfunction.f(x,y)==z:
                arr.append([x,y])
                x+=1
                y-=1
            elif customfunction.f(x,y)<z:
                x+=1
            else:
                y-=1
        return arr
