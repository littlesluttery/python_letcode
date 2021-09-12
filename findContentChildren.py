'''

假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

贪心算法：将排序完的数组，按照饼干最大满足小孩胃口最大。
'''


class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        count = 0
        start = len(s) -1
        for index in range(len(g)-1,-1,-1):
            print(index)
            if start >= 0 and g[index]<=s[start]:
                count += 1
                start -= 1
        print(count)
        return count


f = Solution()
g = [1,2,3]   # 孩子胃口
s = [1,1]    # 饼干能量
f.findContentChildren(g,s)