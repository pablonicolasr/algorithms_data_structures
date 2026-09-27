import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def loga(number: int, base: int) -> int:

    if number // base < base:

        return 1

    else:

        return 1 + loga(number // base, base)


if __name__ == "__main__":

    flag = False

    while not flag:

        try:

            number = int(input("Enter an integer number: \n"))  

            if number > 0:

                flag = True

                print(f"The entered number is: {number}")

                input("Press a key to continue...")

            else:

                print("Please, enter a number greater than 0...")

                input("Press a key to continue...")


        except Exception as e:

            print(e)

            input("Enter an integer number, please...")


    flag2 = False
    
    while not flag2:

        try:

            base = int(input("Enter the base: \n"))  

            if number > 1:

                flag2 = True

                print(f"The base is: {base}")

                input("Press a key to continue...")

            else:

                print("Please, enter a number greater than 1...")

                input("Press a key to continue...")


        except Exception as e:

            print(e)

            input("Enter an integer number, please...")


    print(f"The integer logarithm of {number} to the base {base} is: {loga(number, base)}")