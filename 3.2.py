class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = ''
        while head:
            number = number + str(head.val)
            head = head.next

        return int(number, 2)
