from main import add


def test_add():
    assert add(1, 2) == 3
    assert add(1, 1) == 4


if __name__ == "__main__":
    test_add()
