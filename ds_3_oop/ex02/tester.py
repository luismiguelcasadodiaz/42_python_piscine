from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
print("---------------")
Peter = King("Peter")
print(Peter.__dict__)
Peter.eyes = "blue"
Peter.hairs = "light"
print(Peter.get_eyes())
print(Peter.get_hairs())
print(Peter.__dict__)
