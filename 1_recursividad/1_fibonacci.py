import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")



def fibonacci(number: int) -> int:

    if number == 0:

        return 0

    elif number == 1:

        return 1

    else:

        return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":

    flag = False

    while not flag:

        try:

            number = int(input("Enter a natural number: \n"))

            if number >= 0:

                flag = True

                print(f"The entered number is: {number}")

                input("Press a key to continue...")

        except Exception as e:

            print(e)

            input("Enter a natural number, please...")


    print(f"The result of fibonacci succession in the term {number} is {fibonacci(number)}")

        





