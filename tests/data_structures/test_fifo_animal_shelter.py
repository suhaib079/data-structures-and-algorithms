from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter
def test_addeing_animal():
    new_shelter =AnimalShelter()
    new_shelter.enqueue('jack','dog')
    actual = new_shelter.dog.__str__()
    expected = 'jack-> None'
    assert expected == actual
def test_dequeue_there_is_dogs_and_cats():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('jack','dog')
    new_shelter.enqueue('bsbos','cat')
    actual = new_shelter.dequeue('dog')
    expected = 'jack'
    assert expected == actual
def test_value_other_than_cat_or_dog():
    new_shelter=AnimalShelter()
    actual =new_shelter.dequeue('potato')
    expected = None
    assert expected == actual