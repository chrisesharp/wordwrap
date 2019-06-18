from wordwrap import wrap

def test_wrap_empty_string():
    assert wrap("",1) == ""

def test_wrap_single_word():
    assert wrap("hello",10) == "hello"

def test_wrap_long_word():
    assert wrap("hello",3) == "hel\nlo"

def test_wrap_long_word_multiple_times():
    assert wrap("supercalafragilstic",5) == "super\ncalaf\nragil\nstic"

def test_wrap_two_words():
    assert wrap("hello there",7) == "hello\nthere"

def test_full_monty():
    assert wrap("The quick brown fox jumped over the lazy dog.", 20) == "The quick brown fox\njumped over the lazy\ndog."