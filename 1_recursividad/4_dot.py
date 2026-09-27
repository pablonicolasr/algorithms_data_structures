import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def sign(x: int) -> int:

    return (x > 0) - (x < 0)


def final_sign(sign: int, exponent: int) -> int:

    if sign == 1 or sign == 0:

        return sign

    else:

        if exponent % 2 == 0:

            return 1

        else:

            return -1


def dot(base: int, exponent: int) -> int:

    if exponent == 0:

        return 1

    elif base == 0 and exponent > 0:

        return 0

    else:

        return base * dot(base, exponent - 1)   


if __name__ == "__main__":

    flag1 = False

    while not flag1:

        try:

            base = int(input("Enter base (integer number): \n"))

            flag1 = True

            print(f"The base is: {base}")

            input("Press a key to continue...")

        except Exception as e:

            print(e)

            input("Enter a integer number, please...")

    flag2 = False

    while not flag2:
    
            try:
    
                exponent = int(input("Enter exponent (natural number): \n"))

                if exponent >= 0:    
    
                    flag2 = True

                    print(f"The exponent is: {exponent}")

                    input("Press a key to continue...")
    
            except Exception as e:
    
                print(e)
    
                input("Enter a natural number, please...")


    sign_base = sign(base)

    value_base = abs(base)

    result = dot(value_base, exponent)

    print(f"{base} to the power of {exponent} is {result * final_sign(sign_base, exponent)}")