from bisect import bisect_left, bisect_right
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        start_arr = []
        end_arr = []
        cnt_arr = [0]
        n = len(s)
        i = 0
        while i<n and s[i] == "*" :
            i += 1

        while i < n:
            while i<n and s[i] == "|" :
                i += 1
            start_arr.append(i-1)
            
            while i<n and s[i] == "*" :
                i += 1
            end_arr.append(i)
            cnt_arr.append(end_arr[-1] - start_arr[-1] - 1)
            while i<n and s[i] == "|" :
                i += 1
        
        if len(end_arr)>0 and end_arr[-1] == n:
            end_arr.pop()
            start_arr.pop()
            cnt_arr.pop()
        # print(start_arr, end_arr, cnt_arr)
        
        for i in range(len(cnt_arr)-1):
            cnt_arr[i+1] += cnt_arr[i]

        # print(cnt_arr)
        res = []
        for q in queries:
            l,r = q
            ll = bisect_left(start_arr, l)
            rr = bisect_right(end_arr, r)
            # print(ll, rr)
            # res.append( sum( cnt_arr[ll:rr]) )
            if rr > ll:
                res.append( cnt_arr[rr] - cnt_arr[ll] )
            else:
                res.append(0)
        return res