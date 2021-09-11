class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self,head:ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur!=None):
            temp = cur.next  # 临时保存当前节点的下一个节点
            cur.next = pre   # 反转
            pre = cur        # 更新前指针为当前节点
            cur = temp         # 更新当前指针为之前保存的当前节点的下一个节点
        return pre

