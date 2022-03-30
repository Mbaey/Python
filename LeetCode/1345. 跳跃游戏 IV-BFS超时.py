import numpy as np
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # node = [0] * n
        g  = np.zeros((n, n))

        for i in range(n):
            for j in range(i+1, n):
                # g[i][j]
                if arr[i] == arr[j] and i != j:
                    g[i][j] = 1
                    g[j][i] = 1
            
            if i-1 >= 0 and i-1<n:
                g[i][i-1] = 1
                g[i-1][i] = 1
            if i+1 >= 0 and i+1<n:
                g[i][i+1] = 1
                g[i+1][i] = 1
        # print(g)
        vis = [0] * n
        vis[0] = 1
        que = [ [0, 0] ]

        while que:
            node, depth = que.pop(0)
            vis[node] = 1
            if node == n-1:
                return depth
            
            for i in range(n-1, -1, -1):
                if g[node][i] == 1 and vis[i] == 0:
                    que.append([i, depth+1])
            
            
                    
        # return res