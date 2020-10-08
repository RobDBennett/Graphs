class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        #dummy = node = ListNode()
        prev = None
        while l1 or l2 or carry:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            total += carry
            carry = 0
            if total >= 10:
                total -= 10
                carry += 1
            node = ListNode(total)
            node.next = prev
            prev = node
            #node = node.next
    
        return prev