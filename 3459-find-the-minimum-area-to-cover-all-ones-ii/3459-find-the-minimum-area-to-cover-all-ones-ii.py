class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        return min(self.f(grid), self.f(rotate(grid)))

    def f(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        lr = []  # 每一行最左最右 1 的列号
        for i in range(m):
            l, r = -1, 0
            for j in range(n):
                if a[i][j] > 0:
                    if l < 0:
                        l = j
                    r = j
            lr.append((l, r))

        def minimumArea(a: List[List[int]]) -> List[List[int]]:
            m, n = len(a), len(a[0])
            # f[i+1][j+1] 表示包含【左上角为 (0,0) 右下角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
            f = [[0] * (n + 1) for _ in range(m + 1)]
            border = [(-1, 0, 0)] * n
            for i, row in enumerate(a):
                left, right = -1, 0
                for j, x in enumerate(row):
                    if x:
                        if left < 0:
                            left = j
                        right = j
                    pre_top, pre_left, pre_right = border[j]
                    if left < 0:  # 这一排目前全是 0
                        f[i + 1][j + 1] = f[i][j + 1]  # 等于上面的结果
                    elif pre_top < 0:  # 这一排有 1，上面全是 0
                        f[i + 1][j + 1] = right - left + 1
                        border[j] = (i, left, right)
                    else:  # 这一排有 1，上面也有 1
                        l = min(pre_left, left)
                        r = max(pre_right, right)
                        f[i + 1][j + 1] = (r - l + 1) * (i - pre_top + 1)
                        border[j] = (pre_top, l, r)
            return f

        # lt[i+1][j+1] = 包含【左上角为 (0,0) 右下角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        lt = minimumArea(a)
        a = rotate(a)
        # lb[i][j+1] = 包含【左下角为 (m-1,0) 右上角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        lb = rotate(rotate(rotate(minimumArea(a))))
        a = rotate(a)
        # rb[i][j] = 包含【右下角为 (m-1,n-1) 左上角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        rb = rotate(rotate(minimumArea(a)))
        a = rotate(a)
        # rt[i+1][j] = 包含【右上角为 (0,n-1) 左下角为 (i,j) 的子矩形】中的所有 1 的最小矩形面积
        rt = rotate(minimumArea(a))

        ans = inf
        if m >= 3:
            for i in range(1, m):
                left, right, top, bottom = n, 0, m, 0
                for j in range(i + 1, m):
                    l, r = lr[j - 1]
                    if l >= 0:
                        left = min(left, l)
                        right = max(right, r)
                        top = min(top, j - 1)
                        bottom = j - 1
                    # 图片上左
                    ans = min(ans, lt[i][n] + (right - left + 1) * (bottom - top + 1) + lb[j][n])

        if m >= 2 and n >= 2:
            for i in range(1, m):
                for j in range(1, n):
                    # 图片上中
                    ans = min(ans, lt[i][n] + lb[i][j] + rb[i][j])
                    # 图片上右
                    ans = min(ans, lt[i][j] + rt[i][j] + lb[i][n])
        return ans

# 顺时针旋转矩阵 90°
def rotate(a: List[List[int]]) -> List[List[int]]:
    return list(zip(*reversed(a)))