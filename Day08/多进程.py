__author__ = "Alien"
# 创建一个进程，并在进程中添加线程
import multiprocessing,time,threading,os,queue

# def thread_run():
#     print(threading.get_ident())
#
# def run(name):
#     time.sleep(2)
#     print("Hello",name)
#     t = threading.Thread(target=thread_run)     # 开启一个进程
#     t.start()                                   # 运行这个进程
#
# if __name__=='__main__':
#     for i in range(10):
#         p = multiprocessing.Process(target=run,args=('Jsion',))
#         p.start()

# 通过父进程创建子进程
# def info(n):
#     #父进程
#     print(n)
#     print('module name:',__name__)
#     print('parent process:',os.getppid())       # 获取父进程pid
#     print('process id:',os.getpid())            # 获取进程本身pid
#     print('\n\n')
#
# def f(n):
#     #子进程
#     info('\033[31;1mfunction f\033[0m')
#     print('Hello',n)
#
# if __name__ == '__main__':
#     info('\033[32;1mmain process line\033[0m')
#     # p = multiprocessing.Process(target=f,args=('Jsion',))
#     p = Process(target=f,args=('Jsion',))
#     p.start()
#     p.join()


# 进程的Queue
# def f(qq):
#     qq.put([1,'Hello'])
#
# if __name__ == '__main__':
#     q = queue.Queue()
#     p = multiprocessing.Process(target=f,args=(q,))
#     p.start()
#     print(q.get())
#     p.join()
