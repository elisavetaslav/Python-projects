import sys
class Poly():
    l = list()
    def __init__(self, *args):
        self.l = list()
        if len(args) == 0:
            self.l = [0]
            return
        if type(args[0]) is list:
            self.l = args[0]
            return
        for al in args:
            self.l.append(al)
    def __str__(self):
        if (len(self.l) == 0):
            return "0"
        s = ""
        for i in range(len(self.l) - 1, -1, -1):
            st = ""
            sign = ""
            deg = ""
            if (i > 1):
                deg = "x^"+str(i)
            elif i == 1:
                deg = "x"
            if (self.l[i] > 0):
                sign = "+"
            elif (self.l[i] < 0):
                sign = "-"
            if (abs(self.l[i]) == 1) :
                if (deg == ""):
                    st = str(round(abs(self.l[i]), 2))
            elif (self.l[i] != 0):
                st = str(round(abs(self.l[i]), 3))
            if (len(s) != 0 and self.l[i] != 0):
                s += " " + sign + " " + st + deg
            elif self.l[i] != 0:
                if (sign == "-"):
                    s += sign
                s += st + deg
        if (len(s) == 0):
            s = "0"
        return s

    def __repr__(self):
        s1 = "'Poly(("
        s2 = "))'"
        if len(self.l) == 0:
            return s1 + "0" + s2
        s = ""
        for i in self.l:
            s += str(i) + ", "
        return s1 + s[:-2] + s2

    def __add__(self, args):
        if isinstance(args, int) or isinstance(args, float):
            poly = Poly([args])
        elif isinstance(args, list):
            poly = Poly(args)
        elif isinstance(args, Poly):
            poly = Poly(args.l)
        l = list()
        for i in range(min(len(self.l), len(poly.l))):
            l.append(self.l[i] + poly.l[i])
        if len(self.l) < len(poly.l):
            for i in range(len(self.l), len(poly.l)):
                l.append(poly.l[i])
        elif len(self.l) > len(poly.l):
            for i in range(len(poly.l), len(self.l)):
                l.append(self.l[i])
        return Poly(l)
    __radd__ = __add__

    def __sub__(self, args):
        if isinstance(args, int) or isinstance(args, float):
            poly = Poly([args])
        elif isinstance(args, list):
            poly = Poly(args)
        elif isinstance(args, Poly):
            poly = Poly(args.l)
        l = list()
        for i in range(min(len(self.l), len(poly.l))):
            l.append(self.l[i] - poly.l[i])
        if len(self.l) < len(poly.l):
            for i in range(len(self.l), len(poly.l)):
                l.append(-poly.l[i])
        elif len(self.l) > len(poly.l):
            for i in range(len(poly.l), len(self.l)):
                l.append(self.l[i])
        return Poly(l)

    def __rsub__(self, args):
        if isinstance(args, int) or isinstance(args, float):
            poly = Poly([args])
        elif isinstance(args, list):
            poly = Poly(args)
        elif isinstance(args, Poly):
            poly = Poly(args.l)
        l = list()
        for i in range(min(len(self.l), len(poly.l))):
            l.append(poly.l[i] - self.l[i])
        if len(self.l) < len(poly.l):
            for i in range(len(self.l), len(poly.l)):
                l.append(poly.l[i])
        elif len(self.l) > len(poly.l):
            for i in range(len(poly.l), len(self.l)):
                l.append(-self.l[i])
        return Poly(l)


    def __eq__(self, args):
        if isinstance(args, int) or isinstance(args, float):
            poly = Poly([args])
        elif isinstance(args, list):
            poly = Poly(args)
        elif isinstance(args, Poly):
            poly = Poly(args.l)
        if len(self.l) != len(poly.l):
            return False
        for i in range(len(poly.l)):
            if (self.l[i] != poly.l[i]):
                return False
        return True


    def __mul__(self, args):
        if isinstance(args, int) or isinstance(args, float):
            poly = Poly([args])
        elif isinstance(args, list):
            poly = Poly(args)
        elif isinstance(args, Poly):
            poly = Poly(args.l)
        l = [0] * (len(self.l) + len(poly.l) - 1)
        for i in range(len(self.l)):
            for j in range(len(poly.l)):
                l[i + j] += self.l[i] * poly.l[j]
        return Poly(l)


    __rmul__ = __mul__
    def degree(self):
        for i in range(len(self.l) - 1, -1, -1):
            if (self.l[i] != 0):
                return i
        return 0

    @classmethod
    def poly_from_str(cls, string):
        s = string.split(" ")
        l = list()
        for i in range(len(s)):
            if len(s[i]) == 0:
                continue
            if s[i].count('.') > 0:
                p = s[i].split('.')
                a = float(p[0]) + float(int(p[1])/ (10 ** len(p[1])))
                l.append(a)
            else:
                l.append(int(s[i]))
        return Poly(l)


exec(sys.stdin.read())
