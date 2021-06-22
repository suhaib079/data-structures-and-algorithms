from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_open():
    actual = multi_bracket_validation('[some string]')
    expected = True
    assert expected== actual

def test_close():
    assert multi_bracket_validation('[') ==False

def test_edge():
    assert multi_bracket_validation('{)') == False