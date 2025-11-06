class complex_no:
    def __init__(self, real=None, img=None):
        if real is None or img is None:
            self.real = int(input("Enter Real fact : "))
            self.img = int(input("Enter Img part : "))
        else:
            self.real = real
            self.img = img

    def show(self):
        if self.img >= 0:
            print("{}+{}i".format(self.real,self.img))
        else:
            print("{}{}i".format(self.real,self.img))

    def __add__(self, other):
        x = self.real + other.real
        y = self.img + other.img
        return complex_no(x, y)

c1 = complex_no()
c2 = complex_no()

c3 = c1 + c2 
c3.show()
