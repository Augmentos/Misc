import threading

def func1(lock):
    lock.acquire()
    print('This is the first function' + threading.current_thread().name)
    
    for i in range(10):
        print(i+1)
    lock.release()
    
def func2(lock):
    lock.acquire()
    print('This is the second function' + threading.current_thread().name)
    for i in range(20):
        print(i+1)
    lock.release()
    
if __name__ == "__main__":
    
    print("This is the main thread: " + threading.current_thread().name)
    lock = threading.Lock()
    t1 = threading.Thread(target=func1, name="t1",args=(lock,))
    t2 = threading.Thread(target=func2, name="t2",args=(lock,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done.")