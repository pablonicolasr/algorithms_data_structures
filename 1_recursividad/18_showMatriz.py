import os

from random import randint


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def showMatrix(matriz: list[list[int]], i: int = 0, j: int = 0) -> None:

    if i == len(matriz):

        return

    if j == len(matriz[i]):

        print("\n")

        return showMatrix(matriz, i + 1, 0)

    print(matriz[i][j], end=" ")

    return showMatrix(matriz, i, j + 1)


if __name__ == "__main__":

    flag = False
    
    while not flag:
    
        try:
        
            n = int(input("Enter the size of matrix: \n"))
            
            if n > 0 and n < 20:
                
                flag = True
                
                print(f"The size of matrix is: {n} x {n}")
            
            else:
            
                print("Please, enter an integer greater than 0....")
                
                input("Please, press any key to continue....")      
        
        except Exception as e:
        
            print("Please, enter an integer greater than 0....")
                
            input("Please, press any key to continue....")

    
    
    matriz = [
        [randint(0, n) for _ in range(0, n)] for _ in range (0, n)
    ]

    print(f"The matriz is: {matriz}")

    showMatrix(matriz)      