import sys
class CommonProperties:
    def __init__(self, data):
        self.data = data
    @property
    def size(self):
        return len(self.data)

    @property
    def max_value(self):
        return max(self.data)

    @property
    def min_value(self):
        return min(self.data)
    def __str__(self):
        return f'My {self.__class__.__name__} data {self.data}'
class DictProperties(CommonProperties):
    @property
    def max_value(self):
        try:
            mm = max(self.data.values())
            mmm = max(self.data.keys())
            return max(mm, mmm)
        except:
            try:
                m = max(self.data.keys())
                return m
            except:
                raise TypeError

    @property
    def min_value(self):
        try:
            mm = min(self.data.values())
            mmm = min(self.data.keys())
            return min(mm, mmm)
        except:
            try:
                m = min(self.data.keys())
                return m
            except:
                raise TypeError
class CustomList(CommonProperties):
    pass

class CustomDict(DictProperties):
    pass

exec(sys.stdin.read())
