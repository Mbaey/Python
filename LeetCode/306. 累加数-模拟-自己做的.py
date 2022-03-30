class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        n = len(num)
        s = 0
        nas,nbs=[],[]
        for na in range(1,n):
            for nb in range(1,n):
                nc = max(na, nb)
                if na + nb + nc <= n:
                    sa = num[s:s+na]
                    sb = num[s+na:s+na+nb]
                    if sa[0] == "0" and na > 1 or sb[0] == "0" and nb > 1:
                        break
                    # "0235813" 措
                    # "102" 对
                    
                    a = int(num[s:s+na])
                    b = int(num[s+na:s+na+nb])
                    c = a + b
                    cs = str(c)
                    # c = int(num[s+na+nb:s+na+nb+nc])
                    if num[s+na+nb:].startswith(cs):
                        nas.append(na), nbs.append(nb)

        # print(nas, nbs)

        for na ,nb in zip(nas, nbs):
            # print(na, nb)
            # na,nb=1,1
            s = 0
            while s+na+nb < n:
                a = int(num[s:s+na])
                b = int(num[s+na:s+na+nb])
                # c = int(num[s+na+nb:s+na+nb+nc])

                c = a + b
                cs = str(c)
                nc = len(cs)

                if int(num[s+na+nb:s+na+nb+nc]) == c:
                    s = s + na
                    na = nb
                    nb = nc
                    # nc = max(na, nb)
                else:
                    break
            # print(s, na, nb, nc)
            if s + na + nb == n:
                return True
        return False
        