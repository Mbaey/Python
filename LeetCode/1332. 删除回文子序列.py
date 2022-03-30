class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        l = [""]
        for i in s:
            l.append(i)
            l.append("")
        imax = 0
        idx = 0
        n = len(l)
        # print(l)
        for i in range(1,n):
            length = 1
            while i+length<n and i-length>=0 and l[i-length] == l[i+length]:
                length += 1
            
            length -= 1

            # print(i, length, i-length)

            if imax < length:
                imax = length
                idx = i - length
        
        # imax = (imax - 1) // 2
        # idx = (idx - 1) // 2
        # if idx % 2 == 0:
        idx = idx // 2
        
        news = s[:idx] + s[idx+imax:]
        # print(imax, idx, n)
        print(news)
        return 1 + self.removePalindromeSub(news)


