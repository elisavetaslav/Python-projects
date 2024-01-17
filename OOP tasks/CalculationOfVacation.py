import sys
import datetime


class Vacations:
    def __init__(self):
        self.v = []

    def parse(self, p):
        return list(reversed(list(map(int, p.split('-')))))

    def abs_d(self, p):
        return (datetime.date(*p) - datetime.date(1, 1, 1)).days

    def update_salary(self, d, v):
        dat = self.parse(d)
        ras = self.abs_d(dat)
        self.v.append((ras, v))
        self.v = sorted(self.v)

    def __call__(self, a, b):
        n = self.abs_d(self.parse(a))
        f = self.abs_d(self.parse(b))

        if not len(self.v) or self.v[0][0] > n:
            return 0

        r = n - 1
        k = 0
        s = 0
        while k < 365 and r >= 0:
            v = 0
            for i in self.v:
                if i[0] <= r:
                    v = i[1]
            s += v
            r -= 1
            if not v:
                break
            k += 1

        if not k:
            return 0
        return (s / k) * (f - n + 1)


exec(sys.stdin.read())