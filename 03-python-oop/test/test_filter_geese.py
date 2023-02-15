from src.bird import Bird
from src.filter_geese import filter_geese


def test_can_build_bird():
    bird = Bird('Tweety', 'canary')
    assert bird.name == 'Tweety'
    assert bird.type == 'canary'

def test_filter_geese_with_no_geese():
    b1 = Bird('Tweety', 'canary')
    b2 = Bird('Orville', 'albatross')
    b3 = Bird('Donald', 'duck')
    birds = [b1, b2, b3]
    assert set(filter_geese(birds)) == set(birds)

def test_filter_geese_with_geese():
    b1 = Bird('Tweety', 'canary')
    b2 = Bird('Untitled', 'goose')
    b3 = Bird('Donald', 'duck')
    b4 = Bird('Gus', 'goose')
    b5 = Bird('Orville', 'albatross')
    birds = [b1, b2, b3, b4, b5]
    assert set(filter_geese(birds)) == set([b1, b3, b5])
