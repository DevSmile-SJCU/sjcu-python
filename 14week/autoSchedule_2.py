# Ref : https://wikidocs.net/137924

import os
import sched
import time

def print_file_list():
    file_list = os.listdir()
    print("Current files in the folder:")
    for file in file_list:
        print(file)
    print("---------------------------")

# 스케줄러 객체 생성
scheduler = sched.scheduler(time.time, time.sleep)

# print_file_list 함수를 15초마다 1번씩 반복 실행하는 작업 예약
def repeat_print_file_list():
    print_file_list()
    scheduler.enter(15, 1, repeat_print_file_list, ())

# 첫 번째 작업 예약
scheduler.enter(15, 1, repeat_print_file_list, ())

# 스케줄러 실행
scheduler.run()
