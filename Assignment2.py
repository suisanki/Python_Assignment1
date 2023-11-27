import sys

def calculator(x,y):
    print(f'\nSum: {float(x+y)}')
    print(f'Difference: {float(x-y)}')
    print(f'Product: {float(x*y)}')
    print(f'Quotient: {float(x//y)}')
    
    return 0

    
    
if __name__ == "__main__":
    x = float(input("Enter the value of x:"))
    y = float(input("Enter the value of y:"))
    
    #Print out error message when either x or y is inf or -inf
    if(abs(x) == float('inf') or abs(y) == float('inf')):
        print("\nCalculation involving infinite number is not supported.")
    
    #Print out error message when either x or y is the smallest number float can handle
    elif(abs(x) == sys.float_info.min or abs(y) == sys.float_info.min):
        print("\nAt least one input is too small. Might not provide reasonable result. Try other numbers.")
    
    #Print out error message when either x or y is the largest number float can handle    
    elif(abs(x) == sys.float_info.max or abs(y) == sys.float_info.max):
        print("\nAt least one input is too large. Might not provide reasonable result. Try other numbers.")
               
    else:
        calculator(x,y)