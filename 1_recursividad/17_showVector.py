import os

from random import randint


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def reverse_array(
    arr: list[int | float],
    arr2: list[int | float] | None = None
) -> list[int | float]:

    if arr2 is None:
        arr2 = []

    if len(arr) == 0:
        return arr2

    arr2.append(arr[-1])

    return reverse_array(arr[:-1], arr2)


if __name__ == "__main__":

    flag = False
    
    while not flag:
    
        try:
        
            n = int(input("Enter the size of vector: \n"))
            
            if n > 0 and n < 20:
                
                flag = True
                
                print(f"The size of vector is: {n}")
            
            else:
            
                print("Please, enter an integer greater than 0....")
                
                input("Please, press any key to continue....")      
        
        except Exception as e:
        
            print("Please, enter an integer greater than 0....")
                
            input("Please, press any key to continue....")

    
    
    vector = [randint(0, n) for _ in range(0, n)]

    print(f"The inverted vector of {vector} is: {reverse_array(vector)}")    
            