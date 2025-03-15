import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        temp = head
        length = 0
        while temp.next is not None:
            length += 1
            temp = temp.next

        mid = math.ceil(length / 2)
        print(mid)

        if head.next is None:
            return head
        elif head.next.next is None:
            return head.next

        noob = head
        i = 0
        while noob.next is not None:
            if i >= mid:
                return noob
            i+=1
            noob = noob.next

#         Input
# head =
# [1,2,3,4,5]
# Stdout
# 2
# Output
# [3,4,5]
# Expected
# [3,4,5]

# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
