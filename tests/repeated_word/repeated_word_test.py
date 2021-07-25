 from repeated_word.repeated_word import repeated_word


def test_string():
    sentance = "most common word in games names : last of us / god of war / gta / counter strick / house of card  / uncharted"
    actual = repeated_word(sentance)
    expected = 'of'
    assert expected == actual


def test_no_repetaetd():
    x = "i dont have any repeated word"
    actual = repeated_word(x)
    expected = None
    assert expected == actual