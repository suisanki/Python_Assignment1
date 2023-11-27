import math

#Find the area of yellow shaded space
def find_yellow_area(L):
#area = area of square - area of circle
   return L**2 - ((L/2)**2 * math.pi)
     
def find_room_circle_area(L, M, N):
    #Side length of the chunk of 4 tiles
    L2 = 2*L
    area = find_yellow_area(L)
    
    #Case when M or N (or both) is not a multiply of L
    if M % L != 0 or N % L != 0:
        print("\nM or N is not multipy of L. Try other numbers.")
        return 0
    
    #Sepalating up by whether complete 4 chunks of tile will fit in length and width of the room
    if M % L2 == 0:
        if N % L2 == 0:
            return float((N // L2) * (M // L2) * area * 2)
        else:
            return float(((N // L2) * (M // L2) * area * 2) + area * (M // L2))
        
    else:
        if N % L2 == 0:
            return float(((N // L2) * (M // L2) * area * 2) + area * (N // L2))
            
        else:
            return float(((N // L2) * (M // L2) * area * 2) + area * (M // L2) + area * (N // L2))

if __name__ == "__main__":
    
    L = int(input("Enter the side length of the tile (in integer):"))
    M = int(input("Enter the length of the room (in integer, and make sure it is multiply of the length of the tile):"))
    N = int(input("Enter the width of the room (in integer, and make sure it is multiply of the length of the tile):"))
    
    if find_room_circle_area(L, M, N) != 0:
        print(f'\nThe area of yellow shaded space in the room is {round(find_room_circle_area(L, M, N),2)}.')
    
    elif L == M and L == N:
        print("\nThere is no yellow shaded space in the room.")
    
    else:
        pass
    