class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
class LinkedList():
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_last(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        iterate = self.head
        while iterate.next:
            iterate = iterate.next
        iterate.next = Node(data,None)
    
    def insert_at_index(self,index,data):
        if index<0 or index==self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_beginning(data)
            return
        cnt = 0
        itr = self.head
        while itr:
            if cnt==index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            cnt += 1
    
    def remove_at_index(self,index):
        if index<0 or index==self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            self.head = self.head.next
        cnt = 0
        itr = self.head
        while itr:
            if cnt == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            cnt +=1
    
    def print_linked_list(self):
        if self.head is None:
            return "Empty Linked list"
        itr = self.head
        result = ""
        while itr:
            result += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        return result


if __name__=="__main__":
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_last(4)
    ll.insert_at_last(5)
    ll.insert_at_last(6)
    ll.insert_at_index(2,3)
    print(ll.print_linked_list())
    ll.remove_at_index(3)
    ll.remove_at_index(3)
    print(ll.print_linked_list())