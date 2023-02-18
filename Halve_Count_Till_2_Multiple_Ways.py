
# Division by 2 project.    
# Program Structure: Main and version based functions. 
# Programming Paradgim: Procedural
# Modules: Used. 

from math import log

# Function 1 function: brute force.   
def num_of_times_halved_till_less_than_two_1(n: int) -> int: 
    """ Halves the number till it's less than two and returns count"""
    i = 0
    while n > 2: 
        n = n / 2
        i += 1
    return i 


# Function 2 function => style 1: math thinking 

# Function 3, 
def num_of_times_halved_till_less_than_two_2(n: int) -> int: 
    """ Halves the number till it's less than two and returns count"""
    cnt = 1
    while n  > 2: 
        n = n >> 1
        cnt += 1
    return cnt
    
def num_of_times_halved_till_less_than_two_3(n: int) -> int: 
    """ Halves the number till it's less than two and returns count"""
    return  int(log(n,2))

def main():
    print("\n-- Program repeated Division by 2 till less than 2 --") 
    captured_input = input("Please Enter a Number, Greater than 2: ")
    try:  
        captured_input = int(captured_input)
        if captured_input > 2:
            return print("Number of repeated division:",num_of_times_halved_till_less_than_two_3(captured_input))
        return print("Integer Needs To Be Greater Than 2.")
    except: 
            print("Ensure Integer Entered.")



if __name__ == '__main__':
    while True:
        main()






