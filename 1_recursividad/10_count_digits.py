import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def count_digits(number: int) -> int:

    if number // 10 == 0:

        return 1

    else:

        return 1 + count_digits(number // 10)


if __name__ == "__main__":

    flag = False

    while not flag:

        try:

            number = int(input("Enter an integer number: \n"))        

            flag = True

            num = abs(number)

            print(f"The entered number is: {number}")

            input("Press a key to continue...")

        except Exception as e:

            print(e)

            input("Enter an integer number, please...")


    print(f"The binary number of {number} is {count_digits(num)}")