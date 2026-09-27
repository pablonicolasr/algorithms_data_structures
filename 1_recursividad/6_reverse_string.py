import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def reverse_string(chars: str) -> str:

    if len(chars) <= 1:

        return chars

    return reverse_string(chars[1:]) + chars[0]


if __name__ == "__main__":    

    chars = str(input("Enter character sequence: \n"))

    print(f"The character sequence is: {chars}")

    input("Press a key to continue...")       

    print(f"The inverse string of {chars} is {reverse_string(chars)}")