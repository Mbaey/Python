class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if r*c != m*n:
            return mat
        
        res = []
        for i in range(m):
            for j in range(n):
                
                val = mat[i][j]
                res.append(val)

        res_ = []

        for i in range(r):
            res_.append(res[i * c: (i + 1) * c])
        
        return res_