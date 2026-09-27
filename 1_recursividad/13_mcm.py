import os


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def mcd(a: int, b: int) -> int:

    if a % b == 0:

        return b
    
    else:
    
        return mcd(b, a % b)       


if __name__ == "__main__":

    flag1 = False
    
    while not flag1:
    
        try:
        
            a = int(input("Enter an integer greater than 0 (a): \n"))
            
            if a > 0:
                
                flag1 = True
                
                print(f"The entered number (a) is: {a}")
            
            else:
            
                print("Please, enter an integer greater than 0....")
                
                input("Please, press any key to continue....")      
        
        except Exception as e:
        
            print("Please, enter an integer greater than 0....")
                
            input("Please, press any key to continue....")

    flag2 = False
    
    while not flag2:
    
        try:
        
            b = int(input("Enter an integer less than number a (b): \n"))
            
            if b < a:
                
                flag2 = True
                
                print(f"The entered number (b) is: {b}")
            
            else:
            
                print(f"Please, enter an integer less than {a} and ....")
                
                input("Please, press any key to continue....")      
        
        except Exception as e:
        
            print("Please, enter an integer greater than 0....")
                
            input("Please, press any key to continue....")


    print(f"The least common multiple of {a} and {b} is: {int(abs(a * b)/(mcd(a, b)))}")    