value = input("Enter something: ")

match value: 
    case "a":
        print("You entered a")
    case "b":
        print("You entered b")
    case _:
        print("You entered something else")
