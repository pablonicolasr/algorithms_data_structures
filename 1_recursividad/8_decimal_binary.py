import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def binary(number: int) -> str:

    if number == 0 or number == 1:

        return str(number)

    else:

        return binary(number // 2) + str(number % 2)


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


    print(f"The binary number of {number} is {binary(number)}")