class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def mergeTwoLists(list1, list2):
    dummy = ListNode()  
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = ListNode(list1.val)
            list1 = list1.next
        else:
            tail.next = ListNode(list2.val)
            list2 = list2.next
        tail = tail.next

 
    while list1:
        tail.next = ListNode(list1.val)
        list1 = list1.next
        tail = tail.next

    while list2:
        tail.next = ListNode(list2.val)
        list2 = list2.next
        tail = tail.next

    return dummy.next  # Head of merged list


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(5)

print_list(mergeTwoLists(list1,list2))
