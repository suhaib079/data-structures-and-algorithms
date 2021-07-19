from data_structures_and_algorithms.hash_table import Hashtable
# import pytest

def test_add_key_value():
    hashtable = Hashtable()
    actual = hashtable.add("suhaib","1996")
    expect = ["suhaib", "1996"]
    assert actual == expect

def test_get_value():
    hashtable = Hashtable()
    hashtable.add('length', 174)
    actual = hashtable.get('length')
    expect = 174
    assert actual == expect

def test_get_none_value():
    hashtable = Hashtable()
    hashtable.add('length', 174)
    actual = hashtable.get('wight')
    expect = None
    assert actual == expect

def test_handle_collision():
    hashtable = Hashtable()
    hashtable.add('fall', 'ground')
    hashtable.add('fall', 'seasons')
    for bucket in hashtable._buckets:
        if bucket:
            actual = str(bucket)
    assert actual == "['fall', 'ground']->['fall', 'seasons']->None"


def test_retrive_collision():
    hashtable = Hashtable()
    hashtable.add("kfc", "chicken")
    hashtable.add("kfc", "the employee")
    actual = [hashtable.get("kfc"), hashtable.get("fired")]
    expect = ["chicken", "the employee"]
    assert actual == expect

def test_contains():
    hashtable = Hashtable()
    hashtable.add("Hello", "its me")
    actual = hashtable.contains('Hello')
    expected = True
    assert actual == expected

    actual2 = hashtable.contains("how")
    expected2 = False
    assert actual2 == expected2

def test_hash_key_in_range():
    expected  = 1024
    hashtable = Hashtable()
    actual = hashtable._hash('house')
    assert actual in range(expected)