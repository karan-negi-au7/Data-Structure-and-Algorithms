class Queue: 
    def __init__(self,max_size=100):
        self.queue_list = []
        self.front = self.rear = -1
        self.max_size = max_size

    def enqueue(self,data):
        if self.rear < self.max_size:
            self.queue_list.append(data)
            self.rear+=1
        else:
            print("Overflow")    
        if self.front == -1:
            self.front+=1

    def dequeue(self):
        if self.front == -1:
            print("Underflow")
        else:
            print(self.queue_list.pop(self.front),"removed successfully")
            if self.rear == 0:
                self.front = self.rear = -1
            else:
                self.rear-=1    

    def front_elem(self):
        if self.front == -1:
            print("None")
            return
        print(self.queue_list[self.front],"is a front element")    

    def rear_elem(self):
        if self.rear == -1:
            print("None") 
            return 
        print(self.queue_list[self.rear],"is a rear element")    
        
    def is_empty(self):
        if self.front < 0:
            print("Empty list")
        else:
            print("List is not empty")
            
    def print_queue(self):
        if self.front == -1:
            print("Empty list")
            return 
        for i in self.queue_list:
            print(i,"",end="")
        print()               

#driver code
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.print_queue()
q.front_elem()
q.rear_elem()
