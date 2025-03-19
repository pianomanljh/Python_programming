def exchange(total) :
    n500 = total//500
    total %= 500
    n100 = total//100
    total %= 100
    n50 = total//50
    total %= 50
    n10 = total//10
    print('500원 동전의 개수: {0}\n100원 동전의 개수: {1}\n50원 동전의 개수: {2}\n10원 동전의 개수: {3}'.format(n500,n100,n50,n10))


def get_integer(prompt) :
    get = int(input(prompt))
    return get

money = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(money)