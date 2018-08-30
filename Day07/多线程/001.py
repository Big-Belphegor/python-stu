__author__ = "Alien"
import threading,time

def run(n):
    print('Cli,Cli',n)
    time.sleep(2)

t1 = threading.Thread(target=run,args=("t1",))
t2 = threading.Thread(target=run,args=("t2",))
# 一共用时2s
t1.start()
t2.start()
# 一共用时4s
run(1)
run(2)