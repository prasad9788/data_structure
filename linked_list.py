class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_the_head(self,data):
        new_node = Node(data,self.head)
        self.head = new_node
    
    def printll(self):
        if self.head == None:
            print("head is null")
            return
        itr = self.head
        string = ''
        while itr:
            string += str(itr.data) + "--->"
            itr = itr.next
        print(string)
    def insert_at_the_end(self,data):
        if self.head == None:
            node = Node(data,None)
            self.head = node
            return
        new_node = Node(data,None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node
    def insert_list_at_the_start(self,data):
        self.head = None
        for i in data:
            self.insert_at_the_end(i)
    
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        
        return count
    def insert_at(self,index,data):
        if (index<= 0 or (index > self.get_length())):
            print("index oout of range")
        if index == 0:
            self.insert_at_the_head(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def remove_at(self,index):
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr =itr.next
            count += 1
    
a=Linkedlist()
a.insert_at_the_head(8)
a.insert_at_the_head(1)
a.insert_at_the_head(2)
a.insert_at_the_head(5)
a.insert_at(2,3)
print(a.get_length())
a.remove_at(2)

a.printll()
