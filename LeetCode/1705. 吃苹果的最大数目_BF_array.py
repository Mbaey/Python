import collections
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res = 0
        today = 0

        eat = [0 for i in range(20000)]
        min_day = 20000
        for i in range(len(days)):

            eat[days[i] - 1] = apples[i]

            min_day = min(min_day, days[i] - 1)
            # print("==========")
            # print(eat[:10])

            for j in range(min_day, 20000):
                if eat[j]>0:
                    res += 1
                    eat[j] -= 1
                    min_day = min(j, min_day)
                    break

            del eat[0]
            eat.append(0)
            min_day -= 1
            # print(eat[:10])               
        # print(eat[:100])
        while True:
            flag = True
            for j in range(min_day, 20000):
                if eat[j]>0:
                    res += 1
                    eat[j] -= 1
                    min_day = min(j, min_day)

                    flag = False
                    break
                    
            del eat[0]
            eat.append(0)
            min_day -= 1

            if flag:
                break
        return res