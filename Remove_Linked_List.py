class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Base case: return the last node as the new head
        
        new_head = self.reverseList(head.next)  # Reverse the rest of the list
        head.next.next = head  # Make next node point to current node
        head.next = None  # Break old link
        
        return new_head  
        # Return new head of the reversed list
