class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, root):
        self.root = root

    def append(self, data):
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data=data)

    def output(self):
        tmp = self.root
        while tmp:
            print(tmp.data, end = " ")
            tmp = tmp.next
        print("")   

    def pop(self):
        tmp = self.root
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None
        
root = Node (10)
ll = LinkedList(root=root)
ll.append(11)
ll.append(12)
ll.append(13)
ll.append(14)
ll.output()
ll.pop()
ll.pop()
ll.output()
