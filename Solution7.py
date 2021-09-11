class Solution:
    def combine(self, n: int, k: int):
        # 保存最终结果
        res  = []
        # 保存中间结果
        path = []
        def backtrack(n,k,index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(index,n+1):
                path.append(i)
                backtrack(n,k,i+1)
                path.pop()
        backtrack(n,k,1)
        return res

s = Solution()
n =4
k =2

s.combine(n,k)