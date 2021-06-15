from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList, zipLists
import pytest



def test_instantiate_linked_list():
    """
    empty linked list
    """
    ll = LinkedList()
    
    assert ll.head == None


def test_str(prep_ll):
   
    assert prep_ll.__str__() == '{emad}->{suhaib}->NULL'

def test_incloud_value(prep_ll):
    """"
     Will return true when finding a value within the linked list that exists
    """
  
    assert prep_ll.includes('emad')
    

def test_incloud_false_value(prep_ll):
    """"
     Will return False when finding a value within the linked list that not exists
    """
   
    assert prep_ll.includes('rama')==False
    
def test_append(app_ll):
    '''
    to check if  can successfully add a node to the end of the linked list
    ''' 
    assert app_ll.head.value == 'suhaib'
    assert app_ll.head.next.value == 'emad'
    assert app_ll.head.next.next == None

def test_insert_before_middle():
    """
      to check if Can successfully insert a node before a node located in the middle of a linked list
    """
    ll = LinkedList()
    ll.append('suhaib')
    ll.append('emad')
    ll.append('rama')
    ll.insert_before('emad', 33)
    assert ll.head.next.value == 33

def test_insert_after_middle():
    """
      to check if Can successfully insert after a node in the middle of the linked list
    """
    ll = LinkedList()
    ll.append('suhaib')
    ll.append('emad')
    ll.append('rama')
    ll.insert_after('emad', 33)
    assert ll.head.next.next.value == 33   


@pytest.fixture
def prep_ll():
    ll = LinkedList()
    ll.insert('suhaib')
    ll.insert('emad')
    return ll

@pytest.fixture
def app_ll():
    ll = LinkedList()
    ll.append('suhaib')
    ll.append('emad')
    return ll

def test_kth_from_end_0():
    '''
    Where k and the length of the list are the same

    '''
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    expected = 1
    actual =ll.kth_from_end(3)
    assert expected == actual
    
def test_kth_from_end_6():
    '''
     Where k is greater than the length of the linked list

    '''
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "list is not that long"
    actual =ll.kth_from_end(6)
    assert expected == actual

def test_kth_from_end_2():
    '''
     Happy Path” where k is not at the end, but somewhere in the middle of the linked list

    ''' 
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 3
    actual =ll.kth_from_end(2)
    assert expected == actual


def test_kth_from_end_size_one():
    '''
     Where the linked list is of a size 1 

    '''
    ll = LinkedList()
    ll.append(1)
    expected = 1
    actual =ll.kth_from_end(0)
    assert expected == actual

def test_kth_from_end_negative():
    '''
     Where k is not a positive intege

    ''' 
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "value must be higher than 0 "
    actual =ll.kth_from_end(-2)
    assert expected == actual
def test_LinkedList_kth_from():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_from_end(0)
    expected = 2
    assert actual == expected

def test_LinkedList_kth():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(1)
    ll.insert(8)
    ll.insert(1)
    actual = ll.kth_from_end(2)
    expected = 8
    assert actual == expected

def test_check_last_value():
    li = LinkedList()
    li.append(3)
    li.append(2)
    li.append(1)
    expected = 3
    actual = li.kth_from_end(3)
    assert actual == expected

def test_linked_list_size_1():
    li = LinkedList()
    li.append(1)
    actual = li.kth_from_end(1)
    expected = 1    
    assert actual == expected

def test_value_in_the_middle():
    li = LinkedList()
    li.append(3)
    li.append(2)
    li.append(1)
    actual = li.kth_from_end(2)
    expected = 3
    assert actual == expected 

# zip test 

def test_zipLists(): 
    list1 = LinkedList() 
    list1.append(1) 
    list1.append(2) 
    list1.append(3) 
    list2 = LinkedList() 
    list2.append('a') 
    list2.append('b') 
    list2.append('c')
    assert zipLists(list1,list2) == "{1}->{a}->{2}->{b}->{3}->{c}->NULL"



# ZIP LIST WHEN AN ARRAY IS LONGER THAN OTHER
def test_zipLists2(): 
    list1 = LinkedList() 
    list1.append(1) 
    list1.append(2) 
    list1.append(3) 
    list1.append(0) 
    list2 = LinkedList() 
    list2.append('a') 
    list2.append('b') 
    list2.append('c')
    assert zipLists(list1,list2) == "{1}->{a}->{2}->{b}->{3}->{c}->{0}->NULL"    



