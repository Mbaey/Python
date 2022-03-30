class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))
        big = []
        small = []
        for i in range(n-1):
            
            if security[i] > security[i+1]:
                big.append(1)
                small.append(0)
            elif security[i] < security[i+1]:
                small.append(1)
                big.append(0)
            else:
                big.append(1)
                small.append(1)

        big_set = set()
        small_set = set()
        length = 0
        for i in range(n-1):
            
            if big[i]:
                length += 1
            else:
                length = 0
            if length >= time:
                big_set.add(i+1)
        
        length = 0
        for i in range(n-2, -1, -1):
            if small[i]:
                length += 1
            else:
                length = 0
            if length >= time:
                small_set.add(i)
        print(big, small)
        print(big_set, small_set)
        return list(small_set & big_set)
            

            