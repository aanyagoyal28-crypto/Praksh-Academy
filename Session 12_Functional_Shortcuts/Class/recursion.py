'''
Recursion : 

def sample:
    //code1
    //code2
    //code3
    sample() - recurrsive point

    

sample() - main starting point

We require a appropriate conditon to terminate the recurrsive lopp

10
9
8
7
6
5
4
3
2
1
0
done
'''
def countdown(number):
    if number<=0:
        print(number)
        print("Done")
    else:
        print(number)
        countdown(number-1)

number = int(input("Enter any number = "))
print("Function started")
countdown(number) #starting point
print("Function ended")



