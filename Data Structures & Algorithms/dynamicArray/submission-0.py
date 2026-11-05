class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity


    def get(self, i: int) -> int:
        if 0 <= i <= self.size:
            return self.array[i]
        
        raise IndexError("Index out of bounce")


    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.array[i] = n
        else:
            raise IndexError("Index out of bounce")

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1
  

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Array is empty")

        last_element = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size -= 1

        return last_element

    def resize(self) -> None:
        self.array.extend([None] * self.capacity)
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity