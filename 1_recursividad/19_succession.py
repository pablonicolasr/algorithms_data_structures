import os

from fractions import Fraction


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def succession(number: int) -> int:

    if number == 1:
    
        return 2
    
    else: 
        
        return number  + 1 / succession(number - 1)


if __name__ == "__main__":

    flag = False
    
    while not flag:
    
        try:
        
            number = int(input("Enter an integer number: \n"))
            
            if number > 0:
                
                flag = True
                
                print(f"The entered number is: {number}")
            
            else:
            
                print("Please, enter an positive integer number....")
                
                input("Please, press any key to continue....")            
                
        
        except Exception as e:
        
            print("Please, enter an integer number....")
                
            input("Please, press any key to continue....")

    print(f"The result of the succession with term {number} is: {Fraction(succession(number))}")    