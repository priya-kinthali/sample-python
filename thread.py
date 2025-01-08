import threading
import time

def print_cube(num):
    print("Thread for cube started")
    time.sleep(1)  # Simulate a time-consuming task
    print("Cube: {}".format(num * num * num))
    print("Thread for cube finished")

def print_square(num):
    print("Thread for square started")
    time.sleep(1)  # Simulate a time-consuming task
    print("Square: {}".format(num * num))
    print("Thread for square finished")

if __name__ == "__main__":
    print("Main thread started")
    
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    print("Starting threads")
    t1.start()
    t2.start()

    print("Waiting for threads to complete")
    t1.join()
    t2.join()

    print("All threads completed")
    print("Done!")