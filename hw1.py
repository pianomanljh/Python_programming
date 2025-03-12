def get_radius(prompt):
    r = int(input(prompt))
    return r

radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')

def get_circle_area() :
    s = radius**2*3.14
    return s

area = get_circle_area()

print('반지름 {0}인 원의 넓이 = 3.14 x {0} x {0} = {1}'.format(radius,area))
    

