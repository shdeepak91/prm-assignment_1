class Validation:
    def __init__(self,a,b,c,d,e,f,g,valid_triangle,invalid_triangle,valid_rectangle,invalid_rectangle):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.valid_triangle = valid_triangle
        self.invalid_triangle = invalid_triangle
        self.valid_rectangle = valid_rectangle
        self.invalid_rectangle = invalid_rectangle

    def Triangle_validation(self):
        if (self.a+ self.b > self.c) or (self.a + self.c > self.b) or (self.b + self.c > self.a):
            return self.valid_triangle
        else:
            return self.invalid_triangle
    def Rectangle_validation(self):
        if (self.d == self.e and self.f == self.g) or (self.d == self.f and self.e == self.g) or(self.d == self.g and self.e == self.f):
            return self.valid_rectangle
        else:
            return self.invalid_rectangle 
x = Validation(3,4,5,2,4,2,4,'valid_triangle', 'invalid_triangle','valid_rectangle', 'invalid_rectangle')
print(x.Triangle_validation())
print(x.Rectangle_validation())