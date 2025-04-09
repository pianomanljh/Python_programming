def read_single_digit(num):
    a = '영일이삼사오육칠팔구'
    print(a[num],end = " ")

def read_number(n):
    n100 = n//100
    if n100 != 0:
        read_single_digit(n100)
    n %= 100
    n10 = n//10
    if n10 != 0 or n100 != 0:
        read_single_digit(n10)
    n %= 10
    if n100 != 0 or n10 != 0 or n != 0:
        read_single_digit(n)
    
get = int(input('세 자리 이하 정수 입력 '))

read_number(get)