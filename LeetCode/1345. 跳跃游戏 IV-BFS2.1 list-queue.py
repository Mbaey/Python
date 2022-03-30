import numpy as np
import collections
# [python中的collections.deque和list的性能 - 知乎](https://zhuanlan.zhihu.com/p/358852737)
# deque是双端队列，双端队列的append（）和pop（）的时间复杂度为O（1），而list的insert（0，value），append以及pop（）的时间复杂度为O（n）。
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # node = [0] * n
        # g  = np.zeros((n, n))
        val2idxs = collections.defaultdict(list)
        for i in range(n):
            val = arr[i]
            val2idxs[val].append(i)
        for k in val2idxs:
            val2idxs[k].reverse()
        
        # print(val2idxs)
        # vis = [0] * n
        # vis[0] = 1
        vis = set()
        vis.add(0)  
        que = collections.deque()      
        que.append([0,0])

        while que:
            node, depth = que.popleft()
            val = arr[node]
            
            if node == n-1:
                return depth
            depth += 1

            for i in val2idxs[val]:
                if i not in vis:
                    vis.add(i)
                    que.append([i, depth])
            del val2idxs[val]
            if node + 1 < n and node + 1 not in vis:
                vis.add(node+1)
                if node + 1 == n-1:
                    return depth
                que.append([node + 1, depth])
            if node - 1 >= 0 and node - 1 not in vis:
                vis.add(node-1)
                que.append([node - 1, depth])
                    
        # return res