# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        k = len(lists)
        matrixLength = 0
        for v in lists:
            head = v
            while head:
                matrixLength += 1
                head = head.next
        dummy = None
        head = None

        orderedListsNum = 0
        while matrixLength != orderedListsNum:
            minimumIndex = -1
            for i in range(k):
                print(i, minimumIndex)
                if lists[i] and (minimumIndex == -1 or lists[i].val < lists[minimumIndex].val):
                    minimumIndex = i
            if not head:
                head = lists[minimumIndex]
                dummy = head
            else:
                head.next = lists[minimumIndex]
                head = head.next


            lists[minimumIndex] = lists[minimumIndex].next
            orderedListsNum += 1
        return dummy
