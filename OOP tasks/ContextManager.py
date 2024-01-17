import sys
import time


class Timer:
    def __enter__(self):
        self.time_spent = time.time()
        return self

    def __exit__(self, *a):
        self.time_spent = time.time() - self.time_spent


exec(sys.stdin.read())
