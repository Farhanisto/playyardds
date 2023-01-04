'''
Problem Statement 
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
If the total number of nodes in the LinkedList is even, return the second middle node.
Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3
Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4
Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        if self.head is None:
            print('List is empty')
            return
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next

    def get_middle_node(self, head):
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value


def main():
    l_list = LinkedList()
    l_list.append(2)
    l_list.append(3)
    l_list.append(4)
    l_list.append(5)
    l_list.append(6)
    # l_list.print_list()
    print(l_list.get_middle_node(l_list))


main()
