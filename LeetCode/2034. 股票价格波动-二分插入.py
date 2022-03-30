import bisect
class StockPrice:

    def __init__(self):
        self.t2s = {}
        self.times = []
        self.stocks = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.t2s: # insert
            bisect.insort_left(self.times, timestamp)
            bisect.insort_left(self.stocks, price)
            self.t2s[timestamp] = price
            
        else:
            pre = self.t2s[timestamp]
            self.t2s[timestamp] = price
            self.stocks.remove(pre)
            bisect.insort_left(self.stocks, price)
        
    def current(self) -> int:
        return self.t2s[self.times[-1]]

    def maximum(self) -> int:
        return self.stocks[-1]

    def minimum(self) -> int:
        return self.stocks[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()