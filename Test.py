#Keanna Figirrad
#CS701
#7.25.23
#Programming Assignment 1
#Program Inputs: Dimensions of a room (length, width, height)
#Program Outputs: Total Area to be painted, gallons of paint and primer needed


a = int(input("Enter length:"))
b = int(input("Enter Width:"))
c = int(input("Enter Height:"))

P = 2*(a*b)
W = P*c
C = a*b
T = C + W
print("Total Area to be painted in Sq. Ft.=" + str(T))

paint = T/350
primer = T/200

print("Gallons of Paint needed:" +str(paint))
print("Gallons of Primer needed:" +str(primer))
