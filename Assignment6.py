


def collatz(number):
    #counter: Keep track of how much step it took
    counter = 0
    
    #Repeat the process till the number turns to 1
    while(number != 1):
        #If it is an even number, devide by two and return & print quotient
        if number % 2 == 0:
            number = number // 2
            print(number)
            counter += 1
        #If it is an odd number, multiply by three and add 1, then return & print result
        else:
            number = number*3 + 1
            print(number)
            counter += 1
    print(f'\n{counter} steps needed to get to 1.')
    
    return 0
    
if __name__ == "__main__":
    x = int(input("LET'S PLAY WITH A COLLATZ SEQUENCE! \n Enter an integer: "))
    collatz(x)
    
    
            
