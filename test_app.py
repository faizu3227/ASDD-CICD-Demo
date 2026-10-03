from app import add, place_order


def test_add():
    assert add(5, 10) == 15


def test_place_order():
    assert place_order() == "Food order placed successfully"