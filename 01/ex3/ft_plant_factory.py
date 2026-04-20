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
    plant_data = [
        ["Rose",      25,  30],
        ["oak" ,     200, 365],
        ["Cactus",     5,  90],
        ["Sunflower", 80,  45],
        ["Fern",      15, 120]
        ]
    plants = [
        Plant(plant_data[0][0], plant_data[0][1], plant_data[0][2]),
        Plant(plant_data[1][0], plant_data[1][1], plant_data[1][2]),
        Plant(plant_data[2][0], plant_data[2][1], plant_data[2][2]),                
        Plant(plant_data[3][0], plant_data[3][1], plant_data[3][2]),
        Plant(plant_data[4][0], plant_data[4][1], plant_data[4][2]),                
        ]

    print("=== Plant Factory Output ===")
    for i in range(5):
        print("Created : ", end="")
        plants[i].show()
    