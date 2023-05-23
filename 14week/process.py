# 추가 : Process의 활용
# https://docs.python.org/ko/3/library/multiprocessing.html
# https://docs.python.org/ko/3/library/subprocess.html

from multiprocessing import Process, Queue
import subprocess
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def fn1(name):
    info('function f')
    print('hello', name)
    
def fn2(q):
    q.put([42, None, 'hello'])
          
if __name__ == '__main__':
    
    print('----- Start (1) -----')
    info('main line')
    p = Process(target=fn1, args=('bob',))
    p.start()
    p.join()
    print('----- Done (1) -----')

    print('----- Start (2) -----')
    q = Queue()
    p = Process(target=fn2, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
    print('----- Done (2) -----')
    
    print('----- Start (3) -----')
    # https://blog.naver.com/PostView.nhn?blogId=sagala_soske&logNo=221280201722
    result = subprocess.call(['python', './06week/dict.py'])
    print(result)
    print('----- Done (3) -----')  