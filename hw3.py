def get_fixed_price(won, per) :
    before = won * 100/(100-per)
    return before

rate = float(input('할인율은? '))

A = float(input('A 상품의 할인된 가격은? '))
price_A = get_fixed_price(A, rate)

B = float(input('B 상품의 할인된 가격은? '))
price_B = get_fixed_price(B, rate)

print('A 상품의 정가는', price_A, '원')
print('B 상품의 정가는', price_B, '원')