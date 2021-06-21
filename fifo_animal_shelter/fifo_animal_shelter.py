class Node:
    def __init__(self, data):     #initiate a node
        self.data = data
        self.next = None

class AnimalShelter :
    def __init__(self):
      self.dog = Queue()
      self.cat = Queue()

    def enqueue(self,name,anmial_type):
        if anmial_type == 'dog':
            self.dog.enqueue(name)
        else:
            self.cat.enqueue(name)



    def dequeue(self,anmial_type):

       if anmial_type == 'dog':
           return self.dog.dequeue()
       elif anmial_type =='cat':
           return self.cat.dequeue()
       else:
            return None


class Dog(AnimalShelter):
    pass


class Cat(AnimalShelter):
    pass


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.elements =[]
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = self.tail = new_node
            self.elements.append(new_node.data)
            return

        self.tail.next = new_node
        self.tail = new_node
        self.elements.append(new_node.data)

    def dequeue(self):
        try:
            temp = self.head
            self.head = temp.next
            if self.head == None:
               self.tail = None
            self.elements.pop(0)
            return temp.data
        except AttributeError as e:
            return "empty"

    def peek(self):
        try:
            return self.head.data
        except AttributeError as e:
            return "empty"


    def __str__(self):
        
        pointer = self.head
        elements = ''
        while pointer:
            elements += f"{pointer.data}-> "
            pointer = pointer.next
        elements += f"{pointer}"
        return elements

    def is_empty(self):
       if not self.head:
           return True
       else :
           return False

if __name__ == "__main__":
    pref1,pref2 = 'dog' ,'cat'
    animal = AnimalShelter()
    animal.enqueue('jack','dog')
    animal.enqueue('bsbos','cat')
    animal.enqueue('smokey','cat')
    animal.enqueue('bill','dog')
    print(animal.dequeue('dog'))
    print(animal.dequeue('cat'))
    print(animal.cat.__str__() , animal.dog.__str__() , sep='  ')
    print(animal.dequeue('dog'))