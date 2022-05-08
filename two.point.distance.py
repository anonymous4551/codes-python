#DISTANCE BETWEEN TWO POINT BY PYTHAGORUS THEOREM.
x1 = int(input("Enter x-coordinate first value : "))
x2 = int(input("Enter x-coordiate second value : "))
y1 = int(input("ENter y-coordinate first value  :"))
y2 = int(input("Enter y-coordinate second value : "))
distance = ((((x2-x1)**2) + ((y2-y1)**2))**0.5)
print("THE DISTANCE  BETWEEN ",(x1,x2), " & ",(y1,y2)," is : ",(distance))