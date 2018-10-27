is_male = False
is_tall = True


if is_male and is_tall:
    print("You are a tall male")

elif is_male and not (is_tall):
    print("you are a short male")

elif not (is_male) and is_tall:
    print("you are not a male, but are tall")

else:
    print("you are neither male not tall or both")

num1 = input("Enter 1st Number: ")
num2 = input("Enter 2nd Number: ")
num3 = input("Enter 3rd Number: ")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(num1, num2, num3))
