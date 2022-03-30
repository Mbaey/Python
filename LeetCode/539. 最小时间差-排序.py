class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minute = []
        inf = 24 * 60
        for i in timePoints:
            h,m = i.split(":")
            h = int(h)
            m = int(m)
            minute.append(h*60 + m)
        
        minute.sort()
        imax = minute[-1]-minute[0] 
        imin = imax
        for i in range(1, len(minute)):
            imin = min(imin, minute[i]- minute[i-1])
            
        # print(minute)
        return min(imin, inf - imax)