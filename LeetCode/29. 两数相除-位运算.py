class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1
        if dividend < 0:
            flag *= -1
            dividend = 0-dividend

        if divisor < 0:
            flag *= -1
            divisor = 0-divisor
        
        res = 0
        if divisor ==1:
            res = dividend
        else:
            a = dividend
            while a >= divisor:
                times=1
                b = divisor
                while a >=  b<<1:
                    b = b << 1
                    times = times << 1
                a -= b
                res += times

        res = res*flag

        # math.clip(-21474836481, 2147483647)
        if res > 2**31-1:
            res = 2**31-1
        if res < -2**31:
            res = -2**31
        return res