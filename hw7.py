shopping_bag = {}
while True:
    item = input('상품명? ')
    if item == '':
        print()
        break
    count = int(input('수량? '))
    shopping_bag[item] = count
    print(f'장바구니에 {item} {count}개가 담겼습니다.\n')
    
print(f'>>> 장바구니 보기: {shopping_bag}')
print()
print('[검색]')
search = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{search}은(는) {shopping_bag[search]}개 담겨 있습니다.')