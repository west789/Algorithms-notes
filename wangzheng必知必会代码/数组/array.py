class MyArray:
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, index: int) -> object:
        return self._data[index]

    def __setitem__(self, key: int, value: int):
        self._data[key] = value

    def __iter__(self):
        for i in self._data:
            yield i

    def __len__(self):
        return len(self._data)

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)

    def print_all(self):
        for item in self._data:
            print(item)


def test_myarray():
    myarray = MyArray(5)
    myarray.insert(0, "55")
    myarray.insert(0, 6)
    myarray.insert(1, 3)
    myarray.insert(3, 9)
    myarray.insert(3, 10)
    assert myarray.insert(0, 100) is False
    assert len(myarray) == 5
    assert myarray.find(1) == 3
    assert myarray.delete(4) is True
    myarray.print_all()


test_myarray()