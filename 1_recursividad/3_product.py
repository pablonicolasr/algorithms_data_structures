import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def sign(x: int) -> int:

    return (x > 0) - (x < 0)

def rule_sign(a: int, b: int) -> int:

    if abs(a + b) == 2:

        return 1

    else:

        return -1

def product(number1: int, number2: int) -> int:

    if number1 == 0 or number2 == 0:

        return 0

    elif number1 == 1:

        return number2

    elif number2 == 1:

        return number1

    else:

        return number1 + product(number1, number2 - 1)


if __name__ == "__main__":

    flag1 = False

    while not flag1:

        try:

            number1 = int(input("Enter an integer number1: \n"))

            flag1 = True

            print(f"The entered number1 is: {number1}")

            input("Press a key to continue...")

        except Exception as e:

            print(e)

            input("Enter an integer number, please...")

    flag2 = False

    while not flag2:
    
            try:
    
                number2 = int(input("Enter an integer number2: \n"))    
    
                flag2 = True

                print(f"The entered number2 is: {number2}")

                input("Press a key to continue...")
    
            except Exception as e:
    
                print(e)
    
                input("Enter an integer number, please...")


    sign1 = sign(number1)

    value1 = abs(number1)

    sign2 = sign(number2)

    value2 = abs(number2)

    result = product(value1, value2)

    rule = rule_sign(sign1, sign2)

    print(f"The product of number {number1} and number {number2} is {result * rule}")