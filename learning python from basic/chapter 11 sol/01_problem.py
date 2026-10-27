class twoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}, Y: {self.j}")


class threeDvector(twoDvector):
    def __init__(self, x, y, k):
        super().__init__(x, y)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a=twoDvector(1, 2)
a.show()
b=threeDvector(5, 4, 3)
b.show()