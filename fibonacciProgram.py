# Python program which checks if a number is in the fibonacci sequence and calculates computation time

import time

def fibonacci_recur(x):
    if x <= 1:
        return x
    else:
        return(fibonacci_recur(x-1) + fibonacci_recur(x-2)) #calculates fibonacci sequence

userinput = int(input("Enter a number: ")) #gets user input


if userinput <= 0:
    print("Enter a positive integer value") #input validation
else:
    print("Fibonacci sequence: ")
    time_start = time.perf_counter() #starts timer
    for i in range(100):
        fibonacci_recur(i) #loops fibonacci function
        if fibonacci_recur(i) == userinput: #checks if user input is in the sequence
            print("This number has been found at position: ", i)
            time_elapsed = (time.perf_counter() - time_start) #gets time elasped
            print("computation time: ", time_elapsed, "secs")


