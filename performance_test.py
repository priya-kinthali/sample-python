import time
import threading

def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

def single_threaded_performance(n, iterations):
    start_time = time.time()
    for _ in range(iterations):
        cpu_bound_task(n)
    end_time = time.time()
    return end_time - start_time

def multi_threaded_performance(n, iterations, num_threads):
    start_time = time.time()
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=cpu_bound_task, args=(n,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    n = 1000000
    iterations = 10
    num_threads = 10

    single_execution_time = single_threaded_performance(n, iterations)
    multi_thread_execution_time = multi_threaded_performance(n, iterations, num_threads)

    print(f"Execution time for single-threaded: {single_execution_time} seconds")
    print(f"Execution time for multi-threaded: {multi_thread_execution_time} seconds")