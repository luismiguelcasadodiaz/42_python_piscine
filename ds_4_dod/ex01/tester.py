from in_out import outer
from in_out import square
from in_out import pow

my_counter = outer(5, square)
print("0.-", my_counter)
print("1.-", my_counter.__closure__)
print("2.-", my_counter.__closure__[0])
print("3.-", my_counter.__closure__[1])
print("4.-", my_counter.__closure__[0].cell_contents)
print("5.-", my_counter.__closure__[1].cell_contents)
print(my_counter())
print("6.-", my_counter.__closure__[0].cell_contents)
print(my_counter())
print("7.-", my_counter.__closure__[0].cell_contents)
print(my_counter())
print("8.-", my_counter.__closure__[0].cell_contents)
print("9.-", my_counter.__closure__[1].cell_contents)
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
