class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        hghs = [0] * n
        temp = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    hghs[j] += 1
                else:
                    hghs[j] = 0

            temp += self.rowcount(hghs)
        
        return temp
    
    def rowcount(self, hghs: List[int]) -> int:
        lst = []
        sum01 = [0] * len(hghs)

        for i, h in enumerate(hghs):
            while lst and hghs[lst[-1]] >= h:
                lst.pop()
                
            if lst:
                left = lst[-1]
                sum01[i] = sum01[left] + h * (i-left)
            else:
                sum01[i] = h * (i+1)

            lst.append(i)

        return sum(sum01)