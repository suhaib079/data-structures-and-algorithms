from typing import List


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
        
        List = []
        current = self.head
        if k < 0:
            return("value must be higher than 0 ")
        while current:
            List.append(current)
            current = current.next
        if len(List) < k:
           return("list is not that long")
        List.reverse()
        if k == len(List):
            k = k -1
        return List[k].value        
def zipLists(list1,list2):
    if not (list1 and list2) :
        return list1 
     
    list3 =LinkedList()
    curr1 =list1.head
    curr2 =list2.head
    while curr1:
        list3.append(curr1.value)
        if curr2:
            list3.append(curr2.value)
            curr2 = curr2.next
        curr1= curr1.next
    while curr2 :
        list3.append(curr2.value)
        curr2 =curr2.next
    return list3.__str__()

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
