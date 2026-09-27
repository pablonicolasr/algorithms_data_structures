import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def sign(x: int) -> int:

    return (x > 0) - (x < 0)


def reverse_number(number: int, accumulated: int = 0) -> int:

    if number == 0:

        return accumulated

    else:
        
        return reverse_number(number // 10, accumulated * 10 + number % 10)


if __name__ == "__main__":

    flag = False

    while not flag:

        try:

            number = int(input("Enter an integer number: \n"))        

            flag = True

            print(f"The integer number is: {number}")

            input("Press a key to continue...")

        except Exception as e:

            print(e)

            input("Enter an integer number, please...")


    sign_number = sign(number)
    
    value_number = abs(number)

    print(f"The reverse number of {number} is {sign_number * reverse_number(value_number)}")