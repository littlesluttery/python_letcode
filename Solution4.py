class Solution:
    def commonChars(self, words) :
        # 定义一个hash保存字符串中所有字符出现的最小次数
        hash = [0] * 26
        # 定义最终保存输出结果的列表，因为会出现多个字符
        result  = []
        # 首先利用首个字符串对hash表进行初始化
        for i in words[0]:
            hash[ord(i)-ord('a')] += 1
        # 计算其他各字符串的个数，并更新字符出现的最小频率
        for i in range(1,len(words)):
            hashOther = [0] * 26
            for j in range(len(words[i])):
                hashOther[ord(words[i][j])-ord('a')] += 1
            # 更新hash
            for k in range(26):
                hash[k] = min(hash[k],hashOther[k])
        # 将最终结果输出
        for i in range(26):
            while hash[i] != 0:
                result.extend(chr(i+ ord('a')))
                hash[i] -= 1
        return result