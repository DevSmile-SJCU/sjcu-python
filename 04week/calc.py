def sum(x, y):
    return x + y

# __name__ 은 현재 모듈의 이름을 담고 있는 내장 변수이다.
# cal.py를 직접 실행하면 __name__은 __main__이 된다.
if __name__=="__main__":
    print(sum(1, 2))

