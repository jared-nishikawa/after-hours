import threading
import time

def powers(p):
    for x in range(10):
        print(p**x)
        print(threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    threads = []
    for p in [2, 3, 5, 7, 11]:
        t = threading.Thread(target=powers, args=(p,))
        t.start()
