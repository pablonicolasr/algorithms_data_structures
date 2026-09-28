import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def square_root(number: int, start: int = 0, end: int = 0) -> int:   

    middle = (start + end) // 2

    if end < start:

        return end

    if middle * middle == number:

        return middle

    elif number < middle * middle:

        return square_root(number, start, middle - 1)

    else:

        return square_root(number, middle + 1, end)      


if __name__ == "__main__":

    flag = False

    while not flag:

        try:

            number = int(input("Enter an integer number: \n"))

            if number >= 0:        

                flag = True            

                print(f"The entered number is: {number}")

                input("Press a key to continue...")

            else:

                print("Please, enter an positive integer number: \n")
                
                input("Enter an integer number, please...")  

        except Exception as e:

            print(e)

            input("Enter an integer number, please...")


    print(f"The integer square root of {number} is {square_root(number, 0, number)}")