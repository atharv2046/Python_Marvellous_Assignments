import time
from threading import Thread
from multiprocessing import Process

def compute_sum():
    total = 0
    for i in range(1, 10_000_001):
        total += i
    return total


def normal_sum():
    start = time.time()
    compute_sum()
    end = time.time()
    print(f"Normal: {end - start:.4f} seconds")

def threading_sum():
    start = time.time()
    t = Thread(target=compute_sum)
    t.start()
    t.join()
    end = time.time()
    print(f"Threading: {end - start:.4f} seconds")

def multiprocessing_sum():
    start = time.time()
    p = Process(target=compute_sum)
    p.start()
    p.join()
    end = time.time()
    print(f"Multiprocessing: {end - start:.4f} seconds")
    
def main():
    normal_sum()
    threading_sum()
    multiprocessing_sum()

if __name__ == "__main__":
    main()