class Stack:
    def __init__(self,max_size=100):
        self.max_size = max_size
        self.cur_size = -1
        self.stack_list = []

    def push(self,data):
        if self.cur_size > self.max_size:
            print("Overflow")
            return 
        self.stack_list.append(data)
        self.cur_size+=1

    def pop(self):
        if self.cur_size<0:
            print("Underflow")
            return    
        elem = self.stack_list.pop()
        print(elem,"Popped out sucessfully")
        self.cur_size-=1

    def peek(self):
        if self.cur_size<=0:
            print("None")
            return  
        print("Peek element is:",self.stack_list[self.cur_size])

    def is_empty(self):
        if self.cur_size<0:
            print("True")
            return
        print("False")  

    def print_stack(self):
        if self.cur_size<0:
            print("Empty Stack")
            return 
        for i in self.stack_list:
            print(i,"",end="")
        print()          

#driver code
s = Stack()
s.print_stack()
s.is_empty()
