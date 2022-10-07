from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.book_frequency = SortedDict()

    def book(self, start: int, end: int) -> int:

        result = current_value = 0

        self.book_frequency[start] = 1 if start not in self.book_frequency else self.book_frequency[start] + 1
        self.book_frequency[end] = -1 if end not in self.book_frequency else self.book_frequency[end] - 1

        for key in self.book_frequency:
            current_value = current_value + self.book_frequency[key]
            result = max(current_value, result)
        return result

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)