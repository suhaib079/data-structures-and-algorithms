from left_join.left_join import left_join
import pytest



def test_left_join():
  synonym = left_join()
  synonym.add('fond', 'enamored')
  synonym.add('wrath', 'anger')
  synonym.add('diligent', 'employed')
  synonym.add('guide', 'garp')
  synonym.add('outfit', 'usher')
  antonym = left_join()
  antonym.add('fond', 'averse')
  antonym.add('wrath', 'delight')
  antonym.add('diligent', 'idle')
  antonym.add('guide', 'follow')
  antonym.add('flow', 'jam')
  assert left_join(synonym,antonym).__str__() =="{['diligent', ['employed', 'idle']]} -> None{['outfit', ['usher', None]]} -> None{['fond', ['enamored', 'averse']]} -> None{['guide', ['garp', 'follow']]} -> None{['wrath', ['anger', 'delight']]} -> None"



