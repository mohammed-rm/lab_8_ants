import threading
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import multiprocessing


def calcul_long():
    n = 1E7
    while n > 0:
        n -= 1


if __name__ == '__main__':
    # Question 1
    # Using normal function
    run_method = 10

    start = time.perf_counter()
    for _ in range(run_method):
        calcul_long()
    finish = time.perf_counter()
    print(f'Finished running function {run_method} times in {round(finish - start, 2)} second(s) without threading')

    # Using threading
    start = time.perf_counter()
    threads = []
    for _ in range(run_method):
        t = threading.Thread(target=calcul_long)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    finish = time.perf_counter()
    print(f'Finished running function {run_method} times in {round(finish - start, 2)} second(s) using threading')

    # Using concurrent.futures threading
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(calcul_long, range(1000))
    finish = time.perf_counter()
    print(f'Finished running function 1000 times in {(finish - start, 2)[0]:.5f} second(s) using concurrent.futures threading')

    # Using multiprocessing
    start = time.perf_counter()
    process = []
    for _ in range(run_method):
        p = multiprocessing.Process(target=calcul_long)
        p.start()
        process.append(p)
    for p in process:
        p.join()
    finish = time.perf_counter()
    print(f'Finished running function {run_method} times in {round(finish - start, 2)} second(s) using multiprocessing')

    # Using concurrent.futures multiprocessing
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(calcul_long, range(1000))
    finish = time.perf_counter()
    print(f'Finished running function 1000 times in {(finish - start, 2)[0]:.5f} second(s) using concurrent.futures multiprocessing')

