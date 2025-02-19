class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node before the head to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy  # Pointer to traverse the list
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Skip the node with val
            else:
                current = current.next  # Move to the next node
        
        return dummy.next  # Return the updated list without dummy node
