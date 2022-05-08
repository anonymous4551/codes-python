year  = int(input("ENter year : "))
if year %  400 ==0 :
    print("This is leap year")
elif year % 100 != 0:
    print("This is not leap year")
elif year % 4 == 0:
    print("This is leap year ")
else:
    print("This is not leap year")
       
