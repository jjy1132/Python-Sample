def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

print()


def print_n_times(value,n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요",5)


print()

#가변매개변수 함수

def print_n_times2(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times2(3,"안녕하세요","즐거운","파이썬 프로그래밍")

print()


#기본매개변수

def print_n_times3(value, n=2):
    for i in range(n):
        print(value)

print_n_times3("안녕하세요")

print()

#키워드매개변수

def print_n_times4(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times4("안녕하세요","즐거운","파이썬 프로그래밍", n=3)
