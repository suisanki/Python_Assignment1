import matplotlib.pyplot as plt

def collatz(number):
    #counter: Keep track of how much step it took
    counter = 0
    
    #Repeat the process till the number turns to 1
    while(number != 1):
        #If it is an even number, devide by two and return & print quotient
        if number % 2 == 0:
            number = number // 2
            counter += 1
        #If it is an odd number, multiply by three and add 1, then return & print result
        else:
            number = number*3 + 1
            counter += 1
    
    return counter


if __name__ == "__main__":
    x_value = []
    y_value= []
    for i in range(1,100000):
        
        x_value.append(i)
        y_value.append(collatz(i))
    
    plt.xlabel("Input number", fontsize=20)
    plt.ylabel("Steps till convergence", fontsize=20)
    plt.scatter(x_value,y_value,s=0.1)
    
    #plt.boxplot(y_value)
          
    