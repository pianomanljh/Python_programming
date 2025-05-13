class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f'({self.x},{self.y})',end='')

    def set(self,x,y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x,self.y)

class Rectangle():
    def __init__(self, ltx, lty, rbx, rby):
        self.lt = Point(ltx, lty)
        self.rb = Point(rbx, rby)
        

    def show(self):
        print('좌측 상단 꼭지점이 ',end='')
        self.lt.show()
        print('이고 우측 하단 꼭지점이 ',end='')
        self.rb.show()
        print('인 사각형입니다. ',end='')


    def getWidth(self):
        x1, y1 = self.lt.get()
        x2, y2 = self.rb.get()
        return x2-x1
    def  getHeight(self):
        x1, y1 = self.lt.get()
        x2, y2 = self.rb.get()
        return y2-y1
    def getArea(self):
        return self.getWidth()*self.getHeight()
    def getPerimeter(self):
        return 2*self.getWidth() + 2*self.getHeight()
        

