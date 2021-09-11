#-*- coding=utf-8 -*-
#@Time : 2021/9/11 12:36 PM
#@Author : 小邋遢
#@File : test.py
#@Software : PyCharm
class Solution:
    def combinationSum(self, candidates, target: int) :
        res = [] # 保存最终结果
        path = [] # 保存中间组合结果
        # 回溯函数
        def trackback(candidates,target,sum,index):
            if sum > target: return # 如果中间和已经大于sum，结束这段代码
            if sum == target:return res.append(path[:])
            for i in range(index,len(candidates)):
                if sum + candidates[i] > target: return
                sum += candidates[i]
                path.append(candidates[i])
                trackback(candidates,target,sum,i)
                sum -= candidates[i]
                path.pop()
        candidates = sorted(candidates)
        trackback(candidates,target,0,0)
        return res