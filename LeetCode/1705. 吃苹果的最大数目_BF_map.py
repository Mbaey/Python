import collections
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res = 0
        today = 0
        # 保质期 2 apple
        day2apple = collections.defaultdict(int)
        new_day2apple = collections.defaultdict(int)
        # day2apple[1] = 0
        # day2apple[2] = 0
        # day2apple.pop(2)
        # print(day2apple)
        day = 0
        while True:
                
            if day < len(apples):
                apple = apples[day]
                if apple != 0:
                    day2apple[days[day]] += apple
                if day2apple == {}:
                    day += 1
                    continue
                
            min_day = 1e5
            # min_day 先吃最快过期的苹果
            for k, v in day2apple.items():
                
                min_day = min(min_day, k)
            
            day2apple[min_day] -= 1
            res += 1
            day += 1
            
            new_day2apple = collections.defaultdict(int)
            for k, v in day2apple.items():
                if v != 0:
                    new_day2apple[k-1] = v
            if 0 in new_day2apple:
                new_day2apple.pop(0) 

            day2apple = new_day2apple
            # print(f"第{day}天", day2apple)
            if day2apple == {} and day >= len(apples):
                break
            # break
        return res