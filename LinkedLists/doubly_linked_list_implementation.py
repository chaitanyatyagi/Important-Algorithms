class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = None
        self.tail.next = None
    
    def insert_at_beginning(self,data):
        node = Node(data)
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def insert_at_last(self,data):
        node = Node(data)
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node

    def insert_at_index(self,index,data):
        if index < 0 or index == self.get_length():
            raise Exception("Invalid Index")
        node = Node(data)
        itr = self.head
        cnt = 0
        while itr:
            if cnt==index-1:
                temp = itr.next
                itr.next = node
                node.prev = itr
                node.next = temp
                temp.prev = node
                break
            itr = itr.next
            cnt += 1
        

    def remove_at_index(self,index):
        if index < 0 or index == self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        itr = self.head
        cnt = 0
        while itr:
            if cnt == index-1:
                temp = itr.next.next
                itr.next = temp
                temp.prev = itr
            itr = itr.next
            cnt += 1

    def print_doubly_linked_list(self):
        if self.head is None:
            return "Empty Linked list"
        itr1,itr2 = self.head,self.tail
        result1,result2 = "",""
        while itr1:
            result1 += str(itr1.data)+' --> ' if itr1.next else str(itr1.data)
            itr1 = itr1.next
        while itr2:
            result2 += str(itr2.data)+' --> ' if itr2.prev else str(itr2.data)
            itr2 = itr2.prev
        print(result1)
        print(result2)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
if __name__=="__main__":
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_last(4)
    ll.insert_at_last(5)
    ll.insert_at_last(6)
    ll.insert_at_index(3,3)
    ll.print_doubly_linked_list()
    ll.remove_at_index(3)
    ll.remove_at_index(3)
    ll.print_doubly_linked_list()