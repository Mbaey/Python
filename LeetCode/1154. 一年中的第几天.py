from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        dt = datetime.strptime(date, '%Y-%m-%d')
        dt0 = datetime.strptime(f"{dt.year}-1-1", '%Y-%m-%d')
        # print(dt)
        # print(dt.year)
        return (dt - dt0).days + 1

if __name__ == "__main__":

    solution = Solution()
    # 270
    print(solution.dayOfYear(
        "2019-01-09"
    ))
