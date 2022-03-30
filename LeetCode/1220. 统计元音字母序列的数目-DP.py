class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a,e,i,o,u=1,1,1,1,1
        mod = 1000000007
        # print(mod)
        for _ in range(1,n):
            na=(e+i+u) % mod
            ne=(a+i) % mod
            ni=(e+o) % mod
            no=i % mod
            nu=(i+o) % mod
            a,e,i,o,u=na,ne,ni,no,nu
            # print(a,e,i,o,u)
        l = (a,e,i,o,u)
        return sum(l) % mod
    