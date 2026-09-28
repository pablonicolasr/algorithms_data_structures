import os

from random import randint


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def sentinel_search(
    arr: list[int],
    target: int,
    pos: int = 0
) -> int:

    if pos == len(arr) - 1:

        return -1

    if arr[pos] == target:

        return pos

    return sentinel_search(arr, target, pos + 1)


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

    target = randint(0, len(arr) * 2 + 1)

    arr.append(target)

    position = sentinel_search(arr, target)

    # Eliminamos el centinela.
    arr.pop()

    if position == -1:
        print(f"El elemento {target} no se encuentra en {arr}")
    else:
        print(f"El elemento {target} se encuentra en la posición {position}.")
        print(f"Vector: {arr}")