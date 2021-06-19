from stacks_and_queues.stacks_and_queues import Node, Stack, Queue
import pytest

stack = Stack()

def test_push():
    stack.push('3')
    actual = stack.top.value
    expect = '3'
    assert actual == expect


def test_multi_values():
    stack.push('hey there')
    actual = stack.__str__()
    expect = 'hey there\n3'
    assert actual == expect

def test_pop():
    assert stack.pop() == 'hey there'
    actual = stack.__str__()
    expect = '3'
    assert actual == expect


def test_multi_pop():
    stack.push('abdennabi')
    stack.push('emad')
    stack.push('suhaib')
    assert stack.__str__() == 'suhaib\nemad\nabdennabi\n3'
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.__str__() == ''

def test_peek():
    stack.push('abdennabi')
    stack.push('emad')
    stack.push('suhaib')
    assert stack.peek() == 'suhaib'

def test_initiate_empty_stack():
    stack2 = Stack()
    assert stack2.__str__() == ''

def test_pop_and_peek_on_empty():
    stack3 = Stack()
    assert stack3.pop() == 'you Can not pop an empty stack'
    assert stack3.peek() == 'you can not peek an empty stack'


queue = Queue()

def test_enqueue():
    queue.enqueue('suhaib')
    assert queue.__str__() == 'suhaib'

def test_enqueue_multiple_values():
    queue.enqueue('abdennabi')
    assert queue.__str__() == 'suhaib\nabdennabi'

def test_dequeue():

    assert queue.dequeue() == 'suhaib'
    assert queue.__str__() == 'abdennabi'

def test_peek_queue():
    queue.enqueue('suhaib')
    queue.enqueue('emad')
    queue.enqueue('r')
    assert queue.peek() == ('abdennabi')

def test_multiple_dequeue():
    assert queue.__str__() == 'abdennabi\nsuhaib\nemad\nr'
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.__str__() == ''

def test_init_queue():
    queue2 = Queue()
    assert queue2.__str__() == ''

def test_peek_empty_queue():
    empty_queue = Queue()
    assert empty_queue.__str__() == ''
    assert empty_queue.peek() == 'Cannot peek from empty queue'