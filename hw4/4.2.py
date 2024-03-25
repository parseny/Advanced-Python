import math
import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

cpu_num = os.cpu_count() or 1


def integrate(f, a, b, *, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate_thr_pool(f, a, b, *, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_jobs
    futures = []
    with ThreadPoolExecutor(max_workers=cpu_num) as executor:
        for i in range(n_jobs):
            start = a + i * step
            end = start + step
            futures.append(executor.submit(integrate, f, start, end, n_iter=int(n_iter / n_jobs)))
    return sum(future.result() for future in futures)


def integrate_proc_pool(f, a, b, *, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_jobs
    futures = []
    with ProcessPoolExecutor(max_workers=cpu_num) as executor:
        for i in range(n_jobs):
            start = a + i * step
            end = start + step
            futures.append(executor.submit(integrate, f, start, end, n_iter=int(n_iter / n_jobs)))
    return sum(future.result() for future in futures)


if __name__ == "__main__":
    for n_jobs in range(1, cpu_num * 2 + 1):
        start_thr = time.time()
        result_thr = integrate_thr_pool(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=10000000)
        end_thr = time.time()
        start_proc = time.time()
        result_proc = integrate_proc_pool(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=10000000)
        end_proc = time.time()
        with open('artefacts/logs.txt', 'a') as file:
            file.write(f"ThreadPoolExecutor, n_jobs={n_jobs}, time={(end_thr - start_thr):.6f}\n")
            file.write(f"ProcessPoolExecutor, n_jobs={n_jobs}, time={(end_thr - start_thr):.6f}\n")
