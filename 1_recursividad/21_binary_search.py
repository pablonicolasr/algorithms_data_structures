import os

from random import randint


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def binary_search(
    arr: list[int],
    start: int = 0,
    end: int = 0,
    target: int = None
) -> int:

    middle = (start + end) // 2 

    if end < start:

        return -1

    if arr[middle] == target:
    
        return middle

    elif target < arr[middle]:

        return binary_search(arr, start, middle - 1, target)

    else:

        return binary_search(arr, middle + 1, end, target)

if __name__ == "__main__":

    flag = False
    
    while not flag:
    
        try:
        
            n = int(input("Enter the size of vector: \n"))
            
            if n > 0 and n < 66:
                
                flag = True
                
                print(f"The size of vector is: {n}")
            
            else:
            
                print("Please, enter an integer greater than 0....")
                
                input("Please, press any key to continue....")      
        
        except Exception as e:
        
            print("Please, enter an integer greater than 0....")
                
            input("Please, press any key to continue....")

    
    
    arr = [randint(0, n) for _ in range(0, n)]

    arr.sort()

    target = randint(0, len(arr) * 2 + 1)

    position = binary_search(arr, 0, len(arr) - 1, target)

    if position == -1:

        print(f"El elemento {target} no se encuentra en {arr}")

    else:

        print(f"El elemento {target} se encuentra en la posición {position}.")

        print(f"Vector: {arr}")