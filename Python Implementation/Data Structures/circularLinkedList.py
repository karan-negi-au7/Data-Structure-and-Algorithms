class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self,data):
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next     

        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
        curr_node.next = self.head

    def append(self,data):
        new_node = Node(data)
        curr_node = self.head 
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print((curr_node.data)+"->",end="")
            curr_node = curr_node.next
            if curr_node == self.head:
                print()
                break
        return     
        ''' #2method
        while curr_node.next != self.head:
            print((curr_node.data)+"->",end="")
            curr_node = curr_node.next    
        print(curr_node.data)'''    
           

    def exchangeNodes(self):
        curr = self.head
        while curr.next!=self.head:
            curr = curr.next     
        curr.next.data,curr.data = curr.data,curr.next.data 
        return         


clist = CircularLinkedList()
clist.append("A")
clist.append("B")
clist.append("C")
clist.append("D")
clist.append("E")
clist.prepend("O")
clist.print_list()
clist.exchangeNodes()
clist.print_list()
