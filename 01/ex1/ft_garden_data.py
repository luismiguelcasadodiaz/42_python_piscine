class Plant:

    def __init__(self, name: str, height: int, age: int):
        self._n = name
        self._h = height
        self._a = age

    def show(self):
        print(self._n, ": ", self._h, "cm, ", self._a, " days old", sep="")


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    p1.show()
    p2.show()
    p3.show()
