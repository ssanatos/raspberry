import threading

def first_fun(age):
    while True:
        print("I am first child", age)
    return

def second_fun(age):
    while True:
        print("I am second child",age)
    return

if __name__ == '__main__' :
    first = threading.Thread(target=first_fun, args=(5,))
    second = threading.Thread(target=second_fun, args=(3,))
    # 스레드 활성화
    first.start()
    second.start()
    # 파라미터 설정
    first.daemon = True
    second.daemon = True
    # 스레드 끌어옴
    first.join()
    second.join()

    while True:
        print('I am parent')
    pass