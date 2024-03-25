import time
import sys
from multiprocessing import Process
from threading import Thread

sys.set_int_max_str_digits(0)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        t = a + b
        a, b = b, t
    return t


if __name__ == "__main__":
    p = Process(target=fib, args=(int(1e6),))
    start = time.time()
    p.start()
    p.join()
    end = time.time()
    print(f'{(end - start):3}')

    t = Thread(target=fib, args=(int(1e6),))
    start = time.time()
    t.start()
    t.join()
    end = time.time()
    print(f'{(end - start):.6f}')
