import bisect
import random
import numpy as np
import math
import datetime
import collections
d = datetime.datetime(year=2022, month=1, day=2)
print(d.weekday())

a = math.log2(8)


print(a)


# enumerate
print(chr(97))
print(ord("a"))
print(ord("z"))

print(abs(2-3))

print(math.comb(10, 1))
print(math.comb(10, 2))
print(math.perm(4, 2))


def change():

    a = 8


print(bisect.bisect_left([1, 2, 5], 3))
a = [1, 2, 5]
print(bisect.bisect_left(a[1:], 3))
print(bisect.bisect_left(a, -1))

# bisect.insort_left
# print(np.zeros(100))

# random.randint(0, n-1)

a = [1,2,3]
print(a)
a.remove(2)
print(a)

s = set()
s.add(1)
s.pop()
# collections.defaultdict(list)
a = [1,2,3]
a.reverse()
print(a)


from math import gcd
print(gcd(12, 20))
def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)
print(gcd(40, 20))
# from collections import deque
# q = deque([1,2,3])

# print(q.index(1))
# print(q.pop())
# print(q)
if __name__ == "__main__":
    pass

# solution = Solution()
