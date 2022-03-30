import numpy as np
import collections
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # node = [0] * n
        # g  = np.zeros((n, n))
        val2idxs = collections.defaultdict(list)
        for i in range(n):
            val = arr[i]
            val2idxs[val].append(i)
        # for k in val2idxs:
        #     val2idxs[k].reverse()
        
        # print(val2idxs)
        # vis = [0] * n
        # vis[0] = 1
        vis = set()
        vis.add(0)        
        que = [ [0, 0] ]

        while que:
            node, depth = que.pop(0)
            val = arr[node]
            
            if node == n-1:
                return depth
            

            for i in val2idxs[val]:
                if i not in vis:
                    vis.add(i)
                    que.append([i, depth+1])
            del val2idxs[val]
            if node + 1 < n and node + 1 not in vis:
                vis.add(node+1)
                que.append([node + 1, depth+1])
            if node - 1 >= 0 and node - 1 not in vis:
                vis.add(node-1)
                que.append([node - 1, depth+1])
                    
        # return res