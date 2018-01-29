import io

def test_character():
    f = io.open("task2/input.txt", "r", encoding="utf-8")
    char = list(f.read().strip())
    assert len(char) == 6