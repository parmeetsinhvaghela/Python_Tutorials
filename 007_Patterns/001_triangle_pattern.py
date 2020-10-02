#Triangle pattern
"""
input: 5

Output:

#####
####
###
##
#

"""

#code for pattern: 1
def print_triangle(num):
    cnt = num
    for i in range(num):
        print('#' * cnt)
        cnt -= 1
    return " Pattern printed"
    
    
    
num = int(input('Enter ur input number: '))
print(print_triangle(num))



#code for pattern: 2
"""
input: 5
out put:
    
#
##
###
####
#####

"""

def print_triangle(num):
    cnt = 1
    for i in range(num,0,-1):
        print('#' * cnt)
        cnt += 1
    return " Pattern printed"
    
    
    
num = int(input('Enter ur input number: '))
print(print_triangle(num))


#Add some more patterns and easy way to remember all patterns 

simple left half pyramid

def pyr(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end=" ")
        print("")

pyr(5)


right half pyramid

def pyr(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print("",end=" ")
        k = k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("")
pyr(5)

half triangle
def pyr(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print("",end=" ")
        k = k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("")
pyr(5)

numbers pyramid
def pyr(n):
    """:key
    if we write both num =1 then op will be 1 12 123 1234
    and if we do not write num = 1 upper of j loop the op will be 1 23 456 78910
    """
    num = 1
    for i in range(n):
        num = 1
        for j in range(i+1):
            print(num,end=" ")
            num+=1
        print("")

pyr(5)
print(pyr.__doc__)

characters pyramid

def pyr(n):
    num = 65
    for i in range(0,n):

        for j in range(0,i+1):
            ch = chr(num)
            num += 1
            print(ch, end=" ")
        print(" ")

pyr(5)













