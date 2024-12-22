# Q)1:- write a python program to find the largest among three numbers (using nested if)

# Take input from the user
number1 = int(input("Enter the 1st number: "))
number2 = int(input("Enter the 2nd number: "))
number3 = int(input("Enter the 3rd number: "))


if number1 > number2:
    if number1 > number3:
        max_num = number1
    else:
        max_num = number3
else:
    if number2 > number3:
        max_num = number2
    else:
        max_num = number3

# Print the largest number
print(f"{max_num} is the maximum number")




'''Q)2:-
 a transport company charges the fare according to the following table .
distance   charges
1-50       8 Rs./KM
51-100     10 Rs./KM
>100       12 Rs./KM

write a program to input distance travelled as input and calculate and print the total charge'''



# Input distance travelled

distance = int(input("Enter the number of km travelled: "))

# Checking the distance range and calculate charges 
if distance >= 101:
    charges = distance * 12
    print("The total travel charges are:", charges)
    
elif 51 <= distance <= 100:
    charges = distance * 10
    print("The total travel charges are:", charges)

elif 1 <= distance <= 50:
    charges = distance * 8
    print("The total travel charges are:", charges)

else:
    print("Invalid distance entered")
