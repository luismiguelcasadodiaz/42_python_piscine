# Explores mutability and inmutabilitay of standard data structures

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")    # it is inmutable. I create a new one
ft_set = {"Hello", "tutu!"}      # does not support item assignament. Order
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World"
ft_tuple = ("Hello", "Spain")
ft_set.add("Barcelona!")
ft_set.discard("tutu!")

ft_dict["Hello"] = "42 Barcelona"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
