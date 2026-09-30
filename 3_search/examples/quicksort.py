import os

from random import randint


def clear_screen():

    os.system("cls" if os.name=="nt" else "clear")


def swap(arr, i, j):

    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    
    # choose the pivot
    pivot = arr[high]
    
    # index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1
    
    # traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):

        if arr[j] < pivot:

            i += 1

            swap(arr, i, j)
    
    # move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)

    return i + 1


# the QuickSort function implementation
def quickSort(arr, low, high):

    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)

        quickSort(arr, pi + 1, high)
    

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

    #pivote = randint(0, len(arr) - 2)

    print(f"La lista sin ordenar es: {arr}")

    quickSort(arr, 0, len(arr) - 1)

    print(f"La lista ordenada es: {arr}")