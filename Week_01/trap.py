# 方法3：
class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax, res = 0, 0, 0
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[-1-i])
            res += lmax + rmax - height[i]
        return res - lmax * len(height)


# 方法2：从最高点分成两块，求总面积，然后减去柱子面积，时间复杂度O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        m,minx = 0, 0
        sumh = 0
        for idx,num in enumerate(height):
            sumh += height[idx]
            if num >= m:
                m = num
                minx = idx
        cnt = 0
        maxi, maxj = 0, 0
        for i in range(minx):
            maxi = max(maxi,height[i])
            cnt += maxi
        for j in reversed(range(minx,len(height))):
            maxj = max(maxj,height[j])
            cnt += maxj
        return cnt-sumh


# 方法1：“俄罗斯方块”，超时
class Solution:
    def trap(self, height: List[int]) -> int:  
    n = len(height)
    i, j = 0, n-1
    cnt = 0
    while j-i > 1:
        while i<n and height[i] <= 0:
            i += 1
        while j>-1 and height[j] <= 0:
            j -= 1
        for idx in range(i,j+1):
            height[idx] -= 1
            if height[idx] < 0:
                cnt += 1
    return cnt
