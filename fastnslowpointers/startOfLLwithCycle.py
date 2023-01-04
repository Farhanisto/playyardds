'''
Problem Statement 
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
'''


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detectAndRemoveCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow != fast:
            return False

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
