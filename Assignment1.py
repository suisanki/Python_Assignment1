# Programmer: Ryotaro Takehara
# Date of submission: 10/2/2023

# PSET <Assignment-1>
# ============================================================================

#Problem #1:  Skip numbers
# This program outputs a series of numbers starting from 1 when fed with 
# ending point and step. Ending point is not included in the series.

def generate_by_skipping_1_number(n,step):
    for i in range(1, n, step):
        print(i)
    
if __name__ == "__main__":
    
    #Positive test cases
    #testcase_1
    #generate_by_skipping_1_number(30,2)
    
    #testcase_2
    #generate_by_skipping_1_number(20,3)
    
    #testcase_3
    #generate_by_skipping_1_number(-30,-5)
    
    #testcase_4
    #generate_by_skipping_1_number(-40,-8)

    #Negative test cases
    #testcase_5
    #generate_by_skipping_1_number(30,-2)
    
    #testcase_6
    generate_by_skipping_1_number(10,0.5)

