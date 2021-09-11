class ListNode:
    def __init__(self,val=0,next=None):
        self.val =val
        self.next = next



class Solution2:
    def swapPairs(self,head:ListNode) -> ListNode:
        res = ListNode(head)
        pre = res
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre、cur、post对应最左、中间的、最右边的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next

