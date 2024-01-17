import sys


class ExtendedList(list):
    @property
    def reversed(self):
        return list(reversed(self))

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, a):
        self[0] = a

    @property
    def last(self):
        return self[-1]

    @last.setter
    def last(self, a):
        self[-1] = a

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, a):
        if a > len(self):
            for i in range(a - len(self)):
                self.append(None)
        else:
            del self[a:]


exec(sys.stdin.read())
