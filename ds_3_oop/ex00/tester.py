from S1E9 import Character, Stark


Ned = Stark("Ned")
print("1", Ned.__dict__)
print("2", Ned.is_alive)
Ned.die()
print("3", Ned.is_alive)
print("4", Ned.__doc__)
print("5", Ned.__init__.__doc__)
print("6", Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
