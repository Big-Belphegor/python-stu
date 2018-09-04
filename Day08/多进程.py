__author__ = "Alien"
# 实现多进程，并在进程中添加线程
import multiprocessing,time,threading

def thread_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print("Hello",name)
    t = threading.Thread(target=thread_run)
    t.start()

if __name__=='__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('Jsion',))
        p.start()
