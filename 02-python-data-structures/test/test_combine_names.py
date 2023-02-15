from src.combine_strings import combine_names

def test_combine_names_first_last():
    first_name = 'Ada'
    last_name = 'Lovelace'
    assert combine_names(first_name, last_name) == 'Ada Lovelace'

def test_combine_names_nonsense():
    first_name = 'abc'
    last_name = 'xyz'
    assert combine_names(first_name, last_name) == 'abc xyz'