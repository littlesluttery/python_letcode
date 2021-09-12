#-*- coding=utf-8 -*-
#@Time : 2021/9/12 1:48 PM
#@Author : 小邋遢
#@File : wiggleMaxLength.py
#@Software : PyCharm

'''
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。

'''
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        # 定义前一个差值
        preC= 0
        # 定义当前差值
        curC = 0
        #定义初始峰值
        res = 1
        for i in range(len(nums)-1):
            curC = nums[i+1] - nums[i]
            if curC!=0 and preC*curC <=0:
                res += 1
                preC = curC
        return res



f = Solution()
nums = [1,7,4,9,2,5]
r = f.wiggleMaxLength(nums)

print(r)