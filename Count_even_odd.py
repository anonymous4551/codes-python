list = int(input("Enter a number: "))
even , odd = 0,0
for i in range(list):
    if i % 2:
        even +=  1     #or we can write here :  even = even +1
    else:
        odd +=  1      #or we can write here :  odd = odd- +1
print("even number is : " , even)
print("Odd number is : " , odd)            