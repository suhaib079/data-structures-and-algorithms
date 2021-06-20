class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    
    top = None

    def __init__(self, top=None):
        self.top = top

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

    def push(self, val):
        
        node = Node(val)
        if self.is_empty():
            self.top = node
            node.next = self.top
            self.top = node
        
    def pop(self):
        

        if not self.is_empty():
            self.top = self.top.next
            timed = self.top 
            return timed.data
        return None

    def peek(self):
       

        if not self.is_empty():
            return self.top.data
        return "empty stack"
    
    def is_empty(self):
        
        if self.top == None:
            return True
        return False

class Psuedo_Queue:

    def __init__(self): 
        self.stack_one = Stack()
        self.stack_two = Stack()


    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)


    def enqueue(self, value):
        self.stack_one.push(value)


    def dequeue(self):
        while not self.stack_one.is_empty() : 
            self.stack_two.push(self.stack_one.pop())
        if self.stack_two.is_empty ( ) :
            raise RuntimeError('empty stack') 
        return self.stack_two.pop()


if __name__ == "__main__":

    q_s = Psuedo_Queue()
    q_s.enqueue(4)
    q_s.enqueue(44)
    q_s.enqueue(444)


    q_s.dequeue()
    
    print(q_s.__str__())

class Psuedo_Queue:

    def __init__(self): 
        self.stack_one = Stack()
        self.stack_two = Stack()


    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)


    def enqueue(self, value):
        self.stack_one.push(value)


    def dequeue(self):
        while not self.stack_one.is_empty() : 
            self.stack_two.push(self.stack_one.pop())
        if self.stack_two.is_empty ( ) :
            raise RuntimeError(' empty stack') 
        return self.stack_two.pop()


if __name__ == "__main__":

    q_s = Psuedo_Queue()
    q_s.enqueue(5)
    q_s.enqueue(55)
    q_s.enqueue(555)
    q_s.dequeue()
    
    print(q_s.__str__())