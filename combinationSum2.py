#-*- coding=utf-8 -*-
#@Time : 2021/9/11 2:42 PM
#@Author : 小邋遢
#@File : combinationSum2.py
#@Software : PyCharm
class Solution:
    def combinationSum2(self, candidates, target: int) :
        res = []
        path = []
        def tarckback(candidates,target,sum,index):
            if sum > target: return
            if sum == target:return res.append(path[:])
            for i in range(index,len(candidates)):
                if sum + candidates[i] > target:return
                if i > index and candidates[i] == candidates[i-1] :continue # 将同一层中重复的去除掉
                sum += candidates[i]
                path.append(candidates[i])
                tarckback(candidates,target,sum,i+1)
                sum -= candidates[i]
                path.pop()
        candidates = sorted(candidates)
        tarckback(candidates,target,0,0)
        return res