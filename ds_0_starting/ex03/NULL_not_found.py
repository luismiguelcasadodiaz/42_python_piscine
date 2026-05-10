def NULL_not_found(object: any) -> int:
    #your code here
    if object == None:
        print(f"Nothing: {object} <class 'NoneType'>")
        return 0
    elif object is False:
        print(f"Fake: {object} <class 'bool'>")
        return 0    
    elif object == 0:
        print(f"Zero: {object} <class 'int'>")
        return 0
    elif object == '':
        print(f"Empty: {object} <class 'str'>")
        return 0  
    elif object != object:
        print(f"Cheese: {object} <class 'float'>")
        return 0 
    else:
        print("Type not Found")
    return 1
  