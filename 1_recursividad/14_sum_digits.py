import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def sum_digits(number: int) -> int:

    if number // 10 == 0:
    
        return number
    
    else: 
        
        return number % 10 + sum_digits(number // 10)


if __name__ == "__main__":

    flag = False
    
    while not flag:
    
        try:
        
            number = int(input("Enter an integer number: \n"))
                
            flag = True
                
            print(f"The entered number is: {number}")    
        
        except Exception as e:
        
            print("Please, enter an integer number....")
                
            input("Please, press any key to continue....")

    print(f"The sum of the digits of the integer {number} is: {sum_digits(number)}")    