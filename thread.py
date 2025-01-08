import threading
import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def print_fib(num):
    print(f"Thread for Fibonacci({num}) started")
    result = fib(num)
    print(f"Fibonacci({num}): {result}")
    print(f"Thread for Fibonacci({num}) finished")

if __name__ == "__main__":
    print("Main thread started")
    
    t1 = threading.Thread(target=print_fib, args=(35,))
    t2 = threading.Thread(target=print_fib, args=(35,))

    print("Starting threads")
    start_time = time.time()
    t1.start()
    t2.start()

    print("Waiting for threads to complete")
    t1.join()
    t2.join()
    end_time = time.time()

    print("All threads completed")
    print(f"Done in {end_time - start_time:.2f} seconds!")