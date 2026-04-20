class Plant:

    def __init__(self, name: str, height: float, age: int):
        self._n = name
        self._h = height * 1.0
        self._a = age
        self._daily_g = round(height / age, 1)

    def age(self):
        self._a += 1

    def grow(self):
        self._h += self._daily_g

    def get_height(self):
        return self._h

    def show(self):
        print(self._n, ": ", sep="", end="")
        print(round(self._h, 1), "cm, ", sep="", end="")
        print(self._a, " days old", sep="", )


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    p1.show()
    h_ini = p1.get_height()
    for i in range(1, 8):
        print("=== Day ", i, " ===", sep="")
        p1.age()
        p1.grow()
        p1.show()
    h_fin = p1.get_height()
    print("Growth this week:", round(h_fin - h_ini, 1), "cm", sep="")
