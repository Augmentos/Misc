import threading
x = 0
def func1():
    print('This is the first function' + threading.current_thread().name)
    global x
    for i in range(10):
      x = x + 1
      print(x)
    
def func2():
    print('This is the second function' + threading.current_thread().name)
    global x
    for i in range(10):
          x = x - 1
          print(x)
    
if __name__ == "__main__":
    
    print("This is the main thread: "+threading.current_thread().name)
    t1 = threading.Thread(target=func1, name="t1")
    t2 = threading.Thread(target=func2, name="t2")
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(x , "Done.")