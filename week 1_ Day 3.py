# Q)1:-#using input() function take one number from the user and using ternary operators

 # Take input from the user
num = float(input("Enter a number: "))

# Using ternary operator to check if the number is positive or not
result = "Positive" if num > 0 else "Non-positive"

# Print the result
print(f"The number is {result}.")



# Q)2:- #using the function take two number  and then swap the number

# Take input from the user
a= int(input("Enter the value of 1st number: "))
b= int(input("Enter the value of 2nd number:"))
print("before swapping the value of a and b are :- ",a,b)
t=a
a=b
b=t
print("After swapping the value of a and b:",a,b)
