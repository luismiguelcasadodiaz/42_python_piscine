#This exercices explores mutability and inmutabilitay of standard data strucutures
# 
# 
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")    # it is inmutable. I create a new one
ft_set = {"Hello", "tutu!"}      # does not support item assignament
ft_dict = {"Hello" : "titi!"}
#your code here
print(ft_set)
ft_list[1]="World"
ft_tuple = ("Hello", "Spain")
ft_set.add("Barcelona!")
ft_set.discard("tutu!")

ft_dict["Hello"] = "42 Barcelona"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

print(hash("Hello"))   # ejemplo: 1894580244085487633
print(hash("tutu!"))   # ejemplo: -2685032689226324145
print(hash("Barcelona!"))  # ejemplo:  5765645633518783299