class Solution:
    def isAnagram( self, s: str, t: str) -> bool:
        # 设置hash表
        hash = [0] * 26
        # s = "anagram", t = "nagaram"
        # 将s串中的字符加 1
        for i in range(len(s)):
            hash[ord(s[i])-ord('a')] += 1
        for j in range(len(t)):
            hash[ord(t[j])-ord('a')] -= 1
        print(hash)
        for i in range(26):
            if hash[i]  != 0:
                return False
        return True

so = Solution()
s = 'anagram'
t = 'nagaram'

flag = so.isAnagram(s,t)
print(flag)


