#!/usr/bin/env python3

def ReadTestCase(f , N):
    if N > 0:
        N -= 1
        X = (int)(f.readline())
        if X > 0 and X <= 100:
            arrNumbers = f.readline().split()
            global total
            total = 0
            ReadNumber(f, X, arrNumbers)
            print(total)
            ReadTestCase(f, N)
        else:
            print("Invalid test case")    

def ReadNumber(f , X, arrNumbers):
    if X > 0:
        X -= 1
        n = (int)(arrNumbers[X])
        global total
        if(n > 0):
            total += (n*n)
        ReadNumber(f, X, arrNumbers)   

total = 0
try:
    f = open("input.txt", "r")
    N = (int)(f.readline())
    if N > 0 and N <= 100:   
        ReadTestCase(f, N)
    else:
        print("Invalid number of test case")
    f.close()
except FileNotFoundError:
    print("Input file does not exist")
except:
    print("Unexpected error:", sys.exc_info()[0])
    
