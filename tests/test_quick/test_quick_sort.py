from Quick_Sort.quicksort import quicksort

def test_unsorted_list():
    actual =quicksort([1,5,6,7,8,2,4,55,111],0,8)
    expect = [1, 2, 4, 5, 6, 7, 8, 55, 111]
    assert actual == expect


def test_empty_list():
    actual = quicksort([], 0, -1)
    expect = []
    assert actual == expect