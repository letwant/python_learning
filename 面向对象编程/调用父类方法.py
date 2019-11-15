class A:
    def spam(self):
        print('A.spam')

    def __init__(self):
        self.x = 0

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

    def __init__(self):
        super().__init__()
        self.y = 1

b = B()
b.spam()
print(b.x)