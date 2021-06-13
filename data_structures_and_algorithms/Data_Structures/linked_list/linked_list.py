class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList :
    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value):
        node=Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next=self.head
            self.head=node
        self.size+=1      


    def includes (self,value):
        current=self.head
        while current and current.next != None:
            if current.value == value:
                return True
            current=current.next
        return False


    def __str__(self):
        current=self.head
        result=''

        if current == None:
            return 'Empty List'
        else:
            while current:
                result += f'{{{current.value}}}->'
                current=current.next   
            result += f'NULL'
        return result 

    def append(self, data):
        
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    
    def insert_before(self, value, newvalue):
        '''
        Add a new node with  new Value before the first value node

        '''
        node = Node(newvalue)
        current = self.head
        while current != None:
            if current.value == value:
                node.next = current
                self.head = node
                return
            if current.next:
                if current.next.value == value:
                    node.next = current.next
                    current.next = node
                    return 'secssfuly added'
                current = current.next

    def insert_after(self, value, newvalue):
        '''
        Add a new node with newVal after the first value node

        '''
        node = Node(newvalue)
        current = self.head
        while current != None:
            if current.value == value:
                node.next = current.next
                current.next = node
                return 'secssfuly added'
            current = current.next 

    def kth_from_end(self, k):
        '''
        Return node value (k) from the end of the list

        '''

        try:
                
            n = -1
            current = self.head
            while current:
                current = current.next
                n = n + 1
            if n >= k:
                current = self.head
                for i in range(n - k):
                    current = current.next
            return current.value
        except:
            return "The Value Not Exist"

              







if __name__ == "__main__":
    #pass
    brothers = LinkedList()
    # node1=Node('suhaib')
    # node2=Node('emad')
    # node2.next=node1
    brothers.append('suhaib')
    brothers.append('emad')
    brothers.append('ahmad')
    # brothers.insert('rama')
    print(brothers)
    if brothers.includes('suhaib'): 
        print ('True') 
    else: 
        print ('false')
