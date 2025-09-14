import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if((len(mat)*len(mat[0]))==r*c):
            a=np.reshape(mat,(r,c))
            return a.tolist()

        else:
            return mat