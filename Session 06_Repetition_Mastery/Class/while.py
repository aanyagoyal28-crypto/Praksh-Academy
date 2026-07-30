'''
while - use only when you are unaware of the specific number of iterations
this is condition controlled loop

syntax:
while condition:
    code

    

main drawback of while is it genertes infinite loop if not handled correctly
    
i++
i+=1

loop breaker statement
'''

num = int(input("Enter a number so you can get all even digits till the number = "))#20
i=0
while(i<num):
    print(i)
    i+=1