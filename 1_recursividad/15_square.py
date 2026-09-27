import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def square_root(number: int) -> int: # 100

    if number < 0:

        raise ValueError("Square root of negative number is not defined.")

    if number < 2:

        return number
 
    small_root = square_root(number >> 2)

    guess = small_root << 1

    if (guess + 1) * (guess + 1) <= number:
        
        return guess + 1
    
    return guess    


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


    print(f"The integer square root of {number} is {square_root(number)}")