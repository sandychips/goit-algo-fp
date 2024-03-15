class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def insertion_sort(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head
    while current is not None:
        next_node = current.next
        sorted_head = insert_node(sorted_head, current)
        current = next_node
    return sorted_head

def insert_node(sorted_head, new_node):
    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node

    current = sorted_head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return sorted_head

def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    current = dummy

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1 is not None:
        current.next = head1
    elif head2 is not None:
        current.next = head2

    return dummy.next

# Creating a simple linked list
head = Node(3)
head.next = Node(1)
head.next.next = Node(5)
head.next.next.next = Node(2)

print("Original list:")
print_list(head)

# Reversing the linked list
reversed_head = reverse_linked_list(head)
print("\nReversed list:")
print_list(reversed_head)

# Sorting the linked list using insertion sort
sorted_head = insertion_sort(reversed_head)
print("\nSorted list:")
print_list(sorted_head)

# Creating two sorted linked lists
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

print("\nFirst sorted list:")
print_list(list1)
print("Second sorted list:")
print_list(list2)

# Merging the two sorted linked lists
merged_list = merge_sorted_lists(list1, list2)
print("\nMerged sorted list:")
print_list(merged_list)
