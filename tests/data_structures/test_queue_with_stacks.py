from queue_with_stacks.queue_with_stacks import Psuedo_Queue
import pytest

q = Psuedo_Queue()

def test_enqueue():
    q.enqueue('suhaib')
    q.enqueue('emad')
    q.enqueue('hussen')
   
    actual = q.stack_one.peek()
    assert actual == 'suhaib'


def test_dequeue(): 
    q.enqueue('suhaib')
    q.enqueue('emad')
    q.enqueue('hussen')
   
    actual = q.dequeue()
    assert actual == 'suhaib'


def test_dequeue_2(): 
  q = Psuedo_Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  popped = []
  for _ in range(3):
    popped.append(q.dequeue())
  assert popped == [1, 2, 3]