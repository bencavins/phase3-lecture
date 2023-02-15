from src.array_mean import find_mean

def test_array_mean_with_three_values():
    input_array = [1, 2, 3]
    assert find_mean(input_array) == 2.0

def test_array_mean_with_five_values():
    input_array = [10, 4, 7, 3, 2]
    assert find_mean(input_array) == 5.2

def test_array_mean_with_one_value():
    input_array = [7]
    assert find_mean(input_array) == 7