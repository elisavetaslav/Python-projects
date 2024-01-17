import sys


class ZeroDivisionHandler(Exception):
    def __enter__(self):
        pass

    def __exit__(self, tp, v, p):
        if isinstance(tp, ZeroDivisionError):
            print(v)
            return v
        else:
            return False


exec(sys.stdin.read())